# Function to iterate through all python classes in an application and return the index for subprocess.Popen

def find_subprocess_id(subclass_list: str):
    classes = subclass_list.replace('<class', '').replace('>', '').replace("'", "")
    split_class = classes.split()
    print(split_class)
    count = 0
    for i in split_class:
        count = count+1
        if i == 'subprocess.Popen,':
            return count - 1


classes_string = """
<class 'type'>, <class 'async_generator'>, <class 'int'>, <class
'bytearray_iterator'>, <class 'bytearray'>, <class 'bytes_iterator'>, <class
'bytes'>, <class 'builtin_function_or_method'>, <class 'callable_iterator'>,
<class 'PyCapsule'>, <class 'cell'>, <class 'classmethod_descriptor'>, <class
'classmethod'>, <class 'code'>, <class 'complex'>, <class 'coroutine'>, <class
'dict_items'>, <class 'dict_itemiterator'>, <class 'dict_keyiterator'>, <class
'dict_valueiterator'>, <class 'dict_keys'>, <class 'mappingproxy'>, <class
'dict_reverseitemiterator'>, <class 'dict_reversekeyiterator'>, <class
'dict_reversevalueiterator'>, <class 'dict_values'>, <class 'dict'>, <class
'ellipsis'>, <class 'enumerate'>, <class 'float'>, <class 'frame'>, <class
'frozenset'>, <class 'function'>, <class 'generator'>, <class
'getset_descriptor'>, <class 'instancemethod'>, <class 'list_iterator'>, <class
'list_reverseiterator'>, <class 'list'>, <class 'longrange_iterator'>, <class
'member_descriptor'>, <class 'memoryview'>, <class 'method_descriptor'>, <class
'method'>, <class 'moduledef'>, <class 'module'>, <class 'odict_iterator'>,
<class 'pickle.PickleBuffer'>, <class 'property'>, <class 'range_iterator'>,
<class 'range'>, <class 'reversed'>, <class 'symtable entry'>, <class
'iterator'>, <class 'set_iterator'>, <class 'set'>, <class 'slice'>, <class
'staticmethod'>, <class 'stderrprinter'>, <class 'super'>, <class 'traceback'>,
<class 'tuple_iterator'>, <class 'tuple'>, <class 'str_iterator'>, <class
'str'>, <class 'wrapper_descriptor'>, <class 'types.GenericAlias'>, <class
'anext_awaitable'>, <class 'async_generator_asend'>, <class
'async_generator_athrow'>, <class 'async_generator_wrapped_value'>, <class
'coroutine_wrapper'>, <class 'InterpreterID'>, <class 'managedbuffer'>, <class
'method-wrapper'>, <class 'types.SimpleNamespace'>, <class 'NoneType'>, <class
'NotImplementedType'>, <class 'weakcallableproxy'>, <class 'weakproxy'>, <class
'weakref'>, <class 'types.UnionType'>, <class 'EncodingMap'>, <class
'fieldnameiterator'>, <class 'formatteriterator'>, <class 'BaseException'>,
<class 'hamt'>, <class 'hamt_array_node'>, <class 'hamt_bitmap_node'>, <class
'hamt_collision_node'>, <class 'keys'>, <class 'values'>, <class 'items'>,
<class '_contextvars.Context'>, <class '_contextvars.ContextVar'>, <class
'_contextvars.Token'>, <class 'Token.MISSING'>, <class 'filter'>, <class
'map'>, <class 'zip'>, <class '_frozen_importlib._ModuleLock'>, <class
'_frozen_importlib._DummyModuleLock'>, <class
'_frozen_importlib._ModuleLockManager'>, <class
'_frozen_importlib.ModuleSpec'>, <class '_frozen_importlib.BuiltinImporter'>,
<class '_frozen_importlib.FrozenImporter'>, <class
'_frozen_importlib._ImportLockContext'>, <class '_thread.lock'>, <class
'_thread.RLock'>, <class '_thread._localdummy'>, <class '_thread._local'>,
<class '_io._IOBase'>, <class '_io._BytesIOBuffer'>, <class
'_io.IncrementalNewlineDecoder'>, <class 'posix.ScandirIterator'>, <class
'posix.DirEntry'>, <class '_frozen_importlib_external.WindowsRegistryFinder'>,
<class '_frozen_importlib_external._LoaderBasics'>, <class
'_frozen_importlib_external.FileLoader'>, <class
'_frozen_importlib_external._NamespacePath'>, <class
'_frozen_importlib_external._NamespaceLoader'>, <class
'_frozen_importlib_external.PathFinder'>, <class
'_frozen_importlib_external.FileFinder'>, <class 'codecs.Codec'>, <class
'codecs.IncrementalEncoder'>, <class 'codecs.IncrementalDecoder'>, <class
'codecs.StreamReaderWriter'>, <class 'codecs.StreamRecoder'>, <class
'_abc._abc_data'>, <class 'abc.ABC'>, <class 'collections.abc.Hashable'>,
<class 'collections.abc.Awaitable'>, <class 'collections.abc.AsyncIterable'>,
<class 'collections.abc.Iterable'>, <class 'collections.abc.Sized'>, <class
'collections.abc.Container'>, <class 'collections.abc.Callable'>, <class
'os._wrap_close'>, <class '_sitebuiltins.Quitter'>, <class
'_sitebuiltins._Printer'>, <class '_sitebuiltins._Helper'>, <class
'types.DynamicClassAttribute'>, <class 'types._GeneratorWrapper'>, <class
'warnings.WarningMessage'>, <class 'warnings.catch_warnings'>, <class
'importlib._abc.Loader'>, <class 'itertools.accumulate'>, <class
'itertools.combinations'>, <class 'itertools.combinations_with_replacement'>,
<class 'itertools.cycle'>, <class 'itertools.dropwhile'>, <class
'itertools.takewhile'>, <class 'itertools.islice'>, <class
'itertools.starmap'>, <class 'itertools.chain'>, <class 'itertools.compress'>,
<class 'itertools.filterfalse'>, <class 'itertools.count'>, <class
'itertools.zip_longest'>, <class 'itertools.pairwise'>, <class
'itertools.permutations'>, <class 'itertools.product'>, <class
'itertools.repeat'>, <class 'itertools.groupby'>, <class 'itertools._grouper'>,
<class 'itertools._tee'>, <class 'itertools._tee_dataobject'>, <class
'operator.attrgetter'>, <class 'operator.itemgetter'>, <class
'operator.methodcaller'>, <class 'reprlib.Repr'>, <class 'collections.deque'>,
<class '_collections._deque_iterator'>, <class
'_collections._deque_reverse_iterator'>, <class '_collections._tuplegetter'>,
<class 'collections._Link'>, <class 'functools.partial'>, <class
'functools._lru_cache_wrapper'>, <class 'functools.KeyWrapper'>, <class
'functools._lru_list_elem'>, <class 'functools.partialmethod'>, <class
'functools.singledispatchmethod'>, <class 'functools.cached_property'>, <class
'contextlib.ContextDecorator'>, <class 'contextlib.AsyncContextDecorator'>,
<class 'contextlib._GeneratorContextManagerBase'>, <class
'contextlib._BaseExitStack'>, <class 'enum.auto'>, <enum 'Enum'>, <class
're.Pattern'>, <class 're.Match'>, <class '_sre.SRE_Scanner'>, <class
'sre_parse.State'>, <class 'sre_parse.SubPattern'>, <class
'sre_parse.Tokenizer'>, <class 're.Scanner'>, <class '_csv.Dialect'>, <class
'_csv.reader'>, <class '_csv.writer'>, <class 'csv.Dialect'>, <class
'csv.DictReader'>, <class 'csv.DictWriter'>, <class 'csv.Sniffer'>, <class
'urllib.parse._ResultMixinStr'>, <class 'urllib.parse._ResultMixinBytes'>,
<class 'urllib.parse._NetlocResultMixinBase'>, <class 'pathlib._Flavour'>,
<class 'pathlib._Accessor'>, <class 'pathlib._Selector'>, <class
'pathlib._TerminatingSelector'>, <class 'pathlib.PurePath'>, <class
'zlib.Compress'>, <class 'zlib.Decompress'>, <class '_bz2.BZ2Compressor'>,
<class '_bz2.BZ2Decompressor'>, <class '_lzma.LZMACompressor'>, <class
'_lzma.LZMADecompressor'>, <class '_struct.Struct'>, <class
'_struct.unpack_iterator'>, <class '_weakrefset._IterationGuard'>, <class
'_weakrefset.WeakSet'>, <class 'threading._RLock'>, <class
'threading.Condition'>, <class 'threading.Semaphore'>, <class
'threading.Event'>, <class 'threading.Barrier'>, <class 'threading.Thread'>,
<class 'zipfile.ZipInfo'>, <class 'zipfile.LZMACompressor'>, <class
'zipfile.LZMADecompressor'>, <class 'zipfile._SharedFile'>, <class
'zipfile._Tellable'>, <class 'zipfile.ZipFile'>, <class 'zipfile.Path'>, <class
'textwrap.TextWrapper'>, <class '_random.Random'>, <class '_sha512.sha384'>,
<class '_sha512.sha512'>, <class 'select.poll'>, <class 'select.epoll'>, <class
'selectors.BaseSelector'>, <class '_socket.socket'>, <class 'array.array'>,
<class 'array.arrayiterator'>, <class 'datetime.date'>, <class
'datetime.time'>, <class 'datetime.timedelta'>, <class 'datetime.tzinfo'>,
<class 'calendar._localized_month'>, <class 'calendar._localized_day'>, <class
'calendar.Calendar'>, <class 'calendar.different_locale'>, <class
'email._parseaddr.AddrlistClass'>, <class 'string.Template'>, <class
'string.Formatter'>, <class 'email.charset.Charset'>, <class
'email.header.Header'>, <class 'email.header._ValueFormatter'>, <class
'email._policybase._PolicyBase'>, <class 'email.message.Message'>, <class
'typing._Final'>, <class 'typing._Immutable'>, <class 'typing._TypeVarLike'>,
<class 'typing.Generic'>, <class 'typing._TypingEmpty'>, <class
'typing._TypingEllipsis'>, <class 'typing.Annotated'>, <class
'typing.NamedTuple'>, <class 'typing.TypedDict'>, <class 'typing.NewType'>,
<class 'typing.io'>, <class 'typing.re'>, <class 'importlib.abc.Finder'>,
<class 'importlib.abc.MetaPathFinder'>, <class
'importlib.abc.PathEntryFinder'>, <class 'importlib.abc.ResourceReader'>,
<class 'importlib.metadata.Sectioned'>, <class 'ast.AST'>, <class
'importlib.metadata.Deprecated'>, <class 'importlib.metadata.FileHash'>, <class
'importlib.metadata.Distribution'>, <class
'importlib.metadata.DistributionFinder.Context'>, <class
'importlib.metadata.FastPath'>, <class 'importlib.metadata.Lookup'>, <class
'importlib.metadata.Prepared'>, <class 'markupsafe._MarkupEscapeHelper'>,
<class 'subprocess.CompletedProcess'>, <class 'subprocess.Popen'>, <class
'platform._Processor'>, <class 'socketserver.BaseServer'>, <class
'socketserver.ForkingMixIn'>, <class 'socketserver._NoThreads'>, <class
'socketserver.ThreadingMixIn'>, <class 'socketserver.BaseRequestHandler'>,
<class 'weakref.finalize._Info'>, <class 'weakref.finalize'>, <class
'email.feedparser.BufferedSubFile'>, <class 'email.feedparser.FeedParser'>,
<class 'email.parser.Parser'>, <class 'email.parser.BytesParser'>, <class
'http.client.HTTPConnection'>, <class '_ssl._SSLContext'>, <class
'_ssl._SSLSocket'>, <class '_ssl.MemoryBIO'>, <class '_ssl.SSLSession'>, <class
'_ssl.Certificate'>, <class 'ssl.SSLObject'>, <class 'mimetypes.MimeTypes'>,
<class 'ast.NodeVisitor'>, <class 'dis.Bytecode'>, <class
'tokenize.Untokenizer'>, <class 'inspect.BlockFinder'>, <class
'inspect._void'>, <class 'inspect._empty'>, <class 'inspect.Parameter'>, <class
'inspect.BoundArguments'>, <class 'inspect.Signature'>, <class
'traceback._Sentinel'>, <class 'traceback.FrameSummary'>, <class
'traceback.TracebackException'>, <class 'logging.LogRecord'>, <class
'logging.PercentStyle'>, <class 'logging.Formatter'>, <class
'logging.BufferingFormatter'>, <class 'logging.Filter'>, <class
'logging.Filterer'>, <class 'logging.PlaceHolder'>, <class 'logging.Manager'>,
<class 'logging.LoggerAdapter'>, <class 'werkzeug._internal._Missing'>, <class
'werkzeug.exceptions.Aborter'>, <class 'werkzeug.urls.Href'>, <class
'_hashlib.HASH'>, <class '_hashlib.HMAC'>, <class '_blake2.blake2b'>, <class
'_blake2.blake2s'>, <class 'tempfile._RandomNameSequence'>, <class
'tempfile._TemporaryFileCloser'>, <class 'tempfile._TemporaryFileWrapper'>,
<class 'tempfile.SpooledTemporaryFile'>, <class 'tempfile.TemporaryDirectory'>,
<class 'urllib.request.Request'>, <class 'urllib.request.OpenerDirector'>,
<class 'urllib.request.BaseHandler'>, <class 'urllib.request.HTTPPasswordMgr'>,
<class 'urllib.request.AbstractBasicAuthHandler'>, <class
'urllib.request.AbstractDigestAuthHandler'>, <class
'urllib.request.URLopener'>, <class 'urllib.request.ftpwrapper'>, <class
'http.cookiejar.Cookie'>, <class 'http.cookiejar.CookiePolicy'>, <class
'http.cookiejar.Absent'>, <class 'http.cookiejar.CookieJar'>, <class
'werkzeug.datastructures.ImmutableListMixin'>, <class
'werkzeug.datastructures.ImmutableDictMixin'>, <class
'werkzeug.datastructures._omd_bucket'>, <class
'werkzeug.datastructures.Headers'>, <class
'werkzeug.datastructures.ImmutableHeadersMixin'>, <class
'werkzeug.datastructures.IfRange'>, <class 'werkzeug.datastructures.Range'>,
<class 'werkzeug.datastructures.ContentRange'>, <class
'werkzeug.datastructures.FileStorage'>, <class
'dataclasses._HAS_DEFAULT_FACTORY_CLASS'>, <class 'dataclasses._MISSING_TYPE'>,
<class 'dataclasses._KW_ONLY_TYPE'>, <class 'dataclasses._FIELD_BASE'>, <class
'dataclasses.InitVar'>, <class 'dataclasses.Field'>, <class
'dataclasses._DataclassParams'>, <class 'werkzeug.sansio.multipart.Event'>,
<class 'werkzeug.sansio.multipart.MultipartDecoder'>, <class
'werkzeug.sansio.multipart.MultipartEncoder'>, <class 'pkgutil.ImpImporter'>,
<class 'pkgutil.ImpLoader'>, <class 'unicodedata.UCD'>, <class 'hmac.HMAC'>,
<class 'werkzeug.wsgi.ClosingIterator'>, <class 'werkzeug.wsgi.FileWrapper'>,
<class 'werkzeug.wsgi._RangeWrapper'>, <class 'werkzeug.utils.HTMLBuilder'>,
<class 'werkzeug.wrappers.accept.AcceptMixin'>, <class
'werkzeug.wrappers.auth.AuthorizationMixin'>, <class
'werkzeug.wrappers.auth.WWWAuthenticateMixin'>, <class '_json.Scanner'>, <class
'_json.Encoder'>, <class 'json.decoder.JSONDecoder'>, <class
'json.encoder.JSONEncoder'>, <class 'werkzeug.formparser.FormDataParser'>,
<class 'werkzeug.formparser.MultiPartParser'>, <class
'werkzeug.user_agent.UserAgent'>, <class
'werkzeug.useragents._UserAgentParser'>, <class
'werkzeug.sansio.request.Request'>, <class
'werkzeug.wrappers.request.StreamOnlyMixin'>, <class
'werkzeug.sansio.response.Response'>, <class
'werkzeug.wrappers.response.ResponseStream'>, <class
'werkzeug.wrappers.response.ResponseStreamMixin'>, <class
'werkzeug.wrappers.common_descriptors.CommonRequestDescriptorsMixin'>, <class
'werkzeug.wrappers.common_descriptors.CommonResponseDescriptorsMixin'>, <class
'werkzeug.wrappers.etag.ETagRequestMixin'>, <class
'werkzeug.wrappers.etag.ETagResponseMixin'>, <class
'werkzeug.wrappers.user_agent.UserAgentMixin'>, <class
'werkzeug.test._TestCookieHeaders'>, <class
'werkzeug.test._TestCookieResponse'>, <class 'werkzeug.test.EnvironBuilder'>,
<class 'werkzeug.test.Client'>, <class 'uuid.UUID'>, <class '_pickle.Pdata'>,
<class '_pickle.PicklerMemoProxy'>, <class '_pickle.UnpicklerMemoProxy'>,
<class '_pickle.Pickler'>, <class '_pickle.Unpickler'>, <class
'pickle._Framer'>, <class 'pickle._Unframer'>, <class 'pickle._Pickler'>,
<class 'pickle._Unpickler'>, <class 'jinja2.bccache.Bucket'>, <class
'jinja2.bccache.BytecodeCache'>, <class 'jinja2.utils.MissingType'>, <class
'jinja2.utils.LRUCache'>, <class 'jinja2.utils.Cycler'>, <class
'jinja2.utils.Joiner'>, <class 'jinja2.utils.Namespace'>, <class
'jinja2.nodes.EvalContext'>, <class 'jinja2.nodes.Node'>, <class
'jinja2.visitor.NodeVisitor'>, <class 'jinja2.idtracking.Symbols'>, <class
'jinja2.compiler.MacroRef'>, <class 'jinja2.compiler.Frame'>, <class
'jinja2.runtime.TemplateReference'>, <class 'jinja2.runtime.Context'>, <class
'jinja2.runtime.BlockReference'>, <class 'jinja2.runtime.LoopContext'>, <class
'jinja2.runtime.Macro'>, <class 'jinja2.runtime.Undefined'>, <class
'numbers.Number'>, <class 'jinja2.lexer.Failure'>, <class
'jinja2.lexer.TokenStreamIterator'>, <class 'jinja2.lexer.TokenStream'>, <class
'jinja2.lexer.Lexer'>, <class 'jinja2.parser.Parser'>, <class
'jinja2.environment.Environment'>, <class 'jinja2.environment.Template'>,
<class 'jinja2.environment.TemplateModule'>, <class
'jinja2.environment.TemplateExpression'>, <class
'jinja2.environment.TemplateStream'>, <class 'jinja2.loaders.BaseLoader'>,
<class '__future__._Feature'>, <class 'greenlet.greenlet'>, <class
'werkzeug.local.Local'>, <class 'werkzeug.local.LocalStack'>, <class
'werkzeug.local.LocalManager'>, <class 'werkzeug.local._ProxyLookup'>, <class
'werkzeug.local.LocalProxy'>, <class 'difflib.SequenceMatcher'>, <class
'difflib.Differ'>, <class 'difflib.HtmlDiff'>, <class 'pprint._safe_key'>,
<class 'pprint.PrettyPrinter'>, <class 'werkzeug.routing.RuleFactory'>, <class
'werkzeug.routing.RuleTemplate'>, <class 'werkzeug.routing.BaseConverter'>,
<class 'werkzeug.routing.Map'>, <class 'werkzeug.routing.MapAdapter'>, <class
'gettext.NullTranslations'>, <class 'click._compat._FixupStream'>, <class
'click._compat._AtomicFile'>, <class 'click.utils.LazyFile'>, <class
'click.utils.KeepOpenFile'>, <class 'click.utils.PacifyFlushWrapper'>, <class
'click.types.ParamType'>, <class 'click.parser.Option'>, <class
'click.parser.Argument'>, <class 'click.parser.ParsingState'>, <class
'click.parser.OptionParser'>, <class 'click.formatting.HelpFormatter'>, <class
'click.core.Context'>, <class 'click.core.BaseCommand'>, <class
'click.core.Parameter'>, <class 'blinker._saferef.BoundMethodWeakref'>, <class
'blinker._utilities._symbol'>, <class 'blinker._utilities.symbol'>, <class
'blinker._utilities.lazy_property'>, <class 'blinker.base.Signal'>, <class
'dotenv.parser.Position'>, <class 'dotenv.parser.Reader'>, <class
'dotenv.variables.Atom'>, <class 'dotenv.main.DotEnv'>, <class
'flask.cli.DispatchingApp'>, <class 'flask.cli.ScriptInfo'>, <class
'flask.config.ConfigAttribute'>, <class 'flask.ctx._AppCtxGlobals'>, <class
'flask.ctx.AppContext'>, <class 'flask.ctx.RequestContext'>, <class
'flask.scaffold.Scaffold'>, <class 'itsdangerous.signer.SigningAlgorithm'>,
<class 'itsdangerous.signer.Signer'>, <class
'itsdangerous.serializer.Serializer'>, <class
'itsdangerous._json._CompactJSON'>, <class 'flask.json.tag.JSONTag'>, <class
'flask.json.tag.TaggedJSONSerializer'>, <class
'flask.sessions.SessionInterface'>, <class
'flask.blueprints.BlueprintSetupState'>, <class 'pyexpat.xmlparser'>, <class
'plistlib.UID'>, <class 'plistlib._PlistParser'>, <class
'plistlib._DumbXMLWriter'>, <class 'plistlib._BinaryPlistParser'>, <class
'plistlib._BinaryPlistWriter'>, <class 'pkg_resources.extern.VendorImporter'>,
<class 'pkg_resources._vendor.appdirs.AppDirs'>, <class
'pkg_resources.extern.packaging._structures.InfinityType'>, <class
'pkg_resources.extern.packaging._structures.NegativeInfinityType'>, <class
'pkg_resources.extern.packaging.version._BaseVersion'>, <class
'pkg_resources._vendor.packaging._manylinux._ELFFileHeader'>, <class
'pkg_resources.extern.packaging.tags.Tag'>, <class
'pkg_resources.extern.packaging.specifiers.BaseSpecifier'>, <class
'pkg_resources._vendor.pyparsing._Constants'>, <class
'pkg_resources._vendor.pyparsing._ParseResultsWithOffset'>, <class
'pkg_resources._vendor.pyparsing.ParseResults'>, <class
'pkg_resources._vendor.pyparsing.ParserElement._UnboundedCache'>, <class
'pkg_resources._vendor.pyparsing.ParserElement._FifoCache'>, <class
'pkg_resources._vendor.pyparsing.ParserElement'>, <class
'pkg_resources._vendor.pyparsing._NullToken'>, <class
'pkg_resources._vendor.pyparsing.OnlyOnce'>, <class
'pkg_resources._vendor.pyparsing.pyparsing_common'>, <class
'pkg_resources.extern.packaging.markers.Node'>, <class
'pkg_resources.extern.packaging.markers.Undefined'>, <class
'pkg_resources.extern.packaging.markers.Marker'>, <class
'pkg_resources.extern.packaging.requirements.Requirement'>, <class
'pkg_resources.IMetadataProvider'>, <class 'pkg_resources.WorkingSet'>, <class
'pkg_resources.Environment'>, <class 'pkg_resources.ResourceManager'>, <class
'pkg_resources.NullProvider'>, <class 'pkg_resources.NoDists'>, <class
'pkg_resources.EntryPoint'>, <class 'pkg_resources.Distribution'>, <class
'colorama.ansi.AnsiCodes'>, <class 'colorama.ansi.AnsiCursor'>, <class
'CArgObject'>, <class '_ctypes.CThunkObject'>, <class '_ctypes._CData'>, <class
'_ctypes.CField'>, <class '_ctypes.DictRemover'>, <class
'_ctypes.StructParam_Type'>, <class 'ctypes.CDLL'>, <class
'ctypes.LibraryLoader'>, <class 'colorama.winterm.WinColor'>, <class
'colorama.winterm.WinStyle'>, <class 'colorama.winterm.WinTerm'>, <class
'colorama.ansitowin32.StreamWrapper'>, <class
'colorama.ansitowin32.AnsiToWin32'>
"""


print(find_subprocess_id(classes_string))