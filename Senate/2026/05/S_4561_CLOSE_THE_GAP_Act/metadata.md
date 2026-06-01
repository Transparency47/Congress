# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4561?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4561
- Title: CLOSE THE GAP Act
- Congress: 119
- Bill type: S
- Bill number: 4561
- Origin chamber: Senate
- Introduced date: 2026-05-19
- Update date: 2026-05-29T07:23:31Z
- Update date including text: 2026-05-29T07:23:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-19: Introduced in Senate
- 2026-05-19 - IntroReferral: Introduced in Senate
- 2026-05-19 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S2375-2377)
- Latest action: 2026-05-19: Introduced in Senate

## Actions

- 2026-05-19 - IntroReferral: Introduced in Senate
- 2026-05-19 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S2375-2377)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-19",
    "latestAction": {
      "actionDate": "2026-05-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4561",
    "number": "4561",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "CLOSE THE GAP Act",
    "type": "S",
    "updateDate": "2026-05-29T07:23:31Z",
    "updateDateIncludingText": "2026-05-29T07:23:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S2375-2377)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-05-19T14:53:07Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "WY"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4561is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4561\nIN THE SENATE OF THE UNITED STATES\nMay 19, 2026 Mr. Barrasso (for himself and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo modernize and streamline the permitting process for broadband infrastructure on Federal land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Closing Long Overdue Streamlining Encumbrances To Help Expeditiously Generate Approved Permits Act or the CLOSE THE GAP Act .\n#### 2. Definitions\nIn this Act:\n**(1) Communications facility**\nThe term communications facility has the meaning given the term in section 8705(a) of the Agriculture Improvement Act of 2018 ( 43 U.S.C. 1761a(a) ).\n**(2) Communications site**\nThe term communications site means an area of Federal land available for communications use.\n**(3) Communications use**\nThe term communications use has the meaning given the term in section 8705(a) of the Agriculture Improvement Act of 2018 ( 43 U.S.C. 1761a(a) ).\n**(4) Communications use authorization**\nThe term communications use authorization means an easement, right-of-way, lease, license, or other authorization granted by the Secretary concerned to locate or modify a communications facility on Federal land for the primary purpose of authorizing the occupancy and use of the Federal land for communications use.\n**(5) Cost recovery fee**\nThe term cost recovery fee means any fee collected by a Federal land management agency related to\u2014\n**(A)**\nan application for a communications use authorization; or\n**(B)**\nthe occupancy and use authorized by a communications use authorization pursuant to and consistent with authorizing law.\n**(6) Covered land**\nThe term covered land means land managed by the Secretary concerned.\n**(7) Electronic SF\u2013299**\nThe term electronic SF\u2013299 means a version of Standard Form 299, or a substantially similar form, that has been digitally modified for online interaction.\n**(8) Federal land**\nThe term Federal land means land under the jurisdiction and management of a Federal land management agency.\n**(9) Federal land management agency**\nThe term Federal land management agency means\u2014\n**(A)**\nthe National Park Service;\n**(B)**\nthe Bureau of Land Management;\n**(C)**\nthe Bureau of Reclamation;\n**(D)**\nthe United States Fish and Wildlife Service;\n**(E)**\nthe Bureau of Indian Affairs; and\n**(F)**\nthe Forest Service.\n**(10) Organizational unit**\nThe term organizational unit means\u2014\n**(A)**\nwith respect to Federal land administered by the Secretary of the Interior\u2014\n**(i)**\na State office;\n**(ii)**\na district office;\n**(iii)**\na field office; or\n**(iv)**\na regional office; and\n**(B)**\nwith respect to the Forest Service\u2014\n**(i)**\na regional office;\n**(ii)**\nthe headquarters;\n**(iii)**\nan administrative unit; or\n**(iv)**\na ranger district office.\n**(11) Previously analyzed Federal land**\nThe term previously analyzed Federal land means any Federal land with respect to which the Secretary concerned has\u2014\n**(A)**\ngranted a communications use authorization; and\n**(B)**\nconducted sufficient environmental or historical reviews, as determined by the Secretary concerned.\n**(12) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of the Interior, with respect to Federal land under the jurisdiction and management of the Secretary of the Interior, acting through, as applicable\u2014\n**(i)**\nthe Commissioner of Reclamation;\n**(ii)**\nthe Director of the National Park Service;\n**(iii)**\nthe Director of the United States Fish and Wildlife Service;\n**(iv)**\nthe Director of the Bureau of Land Management; and\n**(v)**\nthe Director of the Bureau of Indian Affairs; and\n**(B)**\nthe Secretary of Agriculture, with respect to National Forest System land, acting through the Chief of the Forest Service.\n**(13) Standard Form 299**\nThe term Standard Form 299 means the form developed by the Administrator of General Services under section 6409(b)(2)(A) of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1455(b)(2)(A) ) or any successor form.\n**(14) Working group**\nThe term working group means the Federal Land Management Agency Working Group established by section 11(a).\n#### 3. Promulgation of regulations for streamlining purposes\n##### (a) Regulations\nNotwithstanding section 6409 of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1455 ), not later than 1 year after the date of enactment of this Act, the Secretary concerned shall promulgate regulations\u2014\n**(1)**\nto ensure, to the maximum extent practicable, that the process is uniform and standardized across applicable organizational units;\n**(2)**\nto require that applications to locate or modify communications facilities on covered land be considered and granted on a competitively neutral, technology neutral, and nondiscriminatory basis; and\n**(3)**\nto require that the cost recovery fee for locating or modifying covered facilities on covered land be\u2014\n**(A)**\ncalculated and assessed on an annual basis; and\n**(B)**\nbased solely on costs incurred by the organizational unit in processing applications and overseeing any construction related thereto.\n##### (b) Requirements\nThe regulations promulgated under subsection (a) shall\u2014\n**(1)**\ninclude procedures for the tracking of applications described in subsection (a)(1), including\u2014\n**(A)**\nidentifying on a publicly available website the number of applications\u2014\n**(i)**\nreceived;\n**(ii)**\napproved; and\n**(iii)**\ndenied;\n**(B)**\nin the case of an application that is denied, requiring that the applicant be provided with\u2014\n**(i)**\na written decision describing the reasons for the denial; and\n**(ii)**\nan opportunity to cure or appeal the denial; and\n**(C)**\ndescribing the period of time between the receipt of an application and the issuance of a final decision on an application; and\n**(2)**\nprovide for minimum lease terms of not less than 30 years for leases with respect to the location of communications facilities on covered land.\n##### (c) Additional considerations\nIn promulgating regulations under subsection (a), the Secretary concerned shall consider\u2014\n**(1)**\nhow discrete reviews in considering an application described in paragraph (1) of that subsection can be conducted simultaneously, rather than sequentially, by any organizational units that must approve the location or modification; and\n**(2)**\nhow to eliminate overlapping requirements among the organizational units with respect to the location or modification of a communications facility on covered land administered by the organizational units.\n##### (d) Communication of streamlined process to organizational units\nThe Secretary concerned shall, with respect to the regulations promulgated under subsection (a)\u2014\n**(1)**\ncommunicate the regulations to the applicable organizational units; and\n**(2)**\nensure that those organizational units follow the regulations.\n##### (e) Savings provisions\n**(1) Real property authorities**\nNothing in this section provides any executive agency or organizational unit with any new leasing or other real property authorities not in existence before the date of enactment of this Act.\n**(2) Effect on other laws**\n**(A) In general**\nNothing in this section, including any action taken pursuant to this section, affects a decision or determination made by any executive agency before the date of enactment of this Act to sell, dispose of, declare excess or surplus, lease, reuse, or redevelop any Federal real property pursuant to title 40, United States Code, the Federal Assets Sale and Transfer Act of 2016 ( 40 U.S.C. 1303 note; Public Law 114\u2013287 ), or any other law governing real property activities of the Federal Government.\n**(B) Agreements**\nNo agreement entered into pursuant to this section obligates the Federal Government to hold, control, or otherwise retain or use real property that may otherwise be deemed as excess, surplus, or that could otherwise be sold, leased, or redeveloped.\n#### 4. Data collection procedures relating to the processing of applications for broadband project permits on Federal land; Report\n##### (a) Definition of applicable deadline\nIn this section, the term applicable deadline , with respect to an application for a broadband project permit on Federal land, means the deadline for that application established by section 6409(b)(3)(A) of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1455(b)(3)(A) ).\n##### (b) Data collection procedures\nNot later than 1 year after the date of enactment of this Act, the Secretaries concerned, acting jointly, shall establish standardized procedures for internally tracking within Federal land management agencies the following data relating to applications for broadband project permits on Federal land:\n**(1)**\nThe number of applications that are pending on or after the applicable deadline.\n**(2)**\nThe number of applications that have been approved by the applicable deadline.\n**(3)**\nThe number of applications that were approved after the applicable deadline.\n**(4)**\nThe number of applications that have been denied by the applicable deadline.\n**(5)**\nThe number of applications that have been denied after the applicable deadline.\n**(6)**\nThe number of applications that have been withdrawn before the applicable deadline.\n**(7)**\nThe number of applications that were withdrawn after the applicable deadline.\n**(8)**\nThe average processing time for applications.\n**(9)**\nIn the case of applications that were approved after the applicable deadline, the average number of days by which the approval exceeded the applicable deadline.\n##### (c) Report on delays in the approval of applications for broadband projects on Federal land\nNot later than 1 year after the date on which the Secretaries concerned establish the procedures under subsection (b), the Secretaries concerned, acting jointly, shall submit to the Committees on Energy and Natural Resources, Environment and Public Works, and Agriculture, Nutrition, and Forestry of the Senate and the Committees on Natural Resources, Energy and Commerce, and Agriculture of the House of Representatives a report that\u2014\n**(1)**\ndescribes and analyzes the data collected in accordance with those procedures, including an analysis of any factors causing a delay in the approval of applications for broadband project permits on Federal land; and\n**(2)**\nprovides recommendations to address any of the factors identified under paragraph (1) in order to accelerate broadband project permitting on Federal land.\n#### 5. Online tracking of application progress\n##### (a) Sense of Congress\nIt is the sense of Congress that communications projects (as defined in section 41001 of the FAST Act ( 42 U.S.C. 4370m )) should be, under title XLI of the FAST Act ( 42 U.S.C. 4370m et seq. ), considered a high priority as having an increased regional or national economic significance.\n##### (b) Communications projects as covered projects\nSection 41001 of the FAST Act ( 42 U.S.C. 4370m ) is amended\u2014\n**(1)**\nby redesignating paragraphs (4) through (18) as paragraphs (5) through (19), respectively;\n**(2)**\nby inserting after paragraph (3) the following:\n(4) Communications project (A) In general The term communications project means any construction project carried out at a communications site. (B) Other terms For purposes of this paragraph: (i) Communications facility The term communications facility has the meaning given the term in section 8705(a) of the Agriculture Improvement Act of 2018 ( 43 U.S.C. 1761a(a) ). (ii) Communications site The term communications site means an area of Federal land available for communications use. (iii) Communications use The term communications use has the meaning given the term in section 8705(a) of the Agriculture Improvement Act of 2018 ( 43 U.S.C. 1761a(a) ). (iv) Federal land The term Federal land means land under the jurisdiction and management of a Federal land management agency. (v) Federal land management agency The term Federal land management agency means\u2014 (I) the National Park Service; (II) the Bureau of Land Management; (III) the Bureau of Reclamation; (IV) the United States Fish and Wildlife Service; (V) the Forest Service; and (VI) the Bureau of Indian Affairs. ; and\n**(3)**\nin paragraph (7)(A) (as so redesignated)\u2014\n**(A)**\nin the matter preceding clause (i), by inserting communications projects, after carbon capture, ; and\n**(B)**\nin clause (i), by striking subclause (II) and inserting the following:\n(II) is likely to require a total investment\u2014 (aa) in the case of a communications project, of any amount; and (bb) in the case of any other activity, of more than $200,000,000; and .\n#### 6. Improving public safety on Federal land\nNot later than 30 days after the date of enactment of this Act, the Secretary concerned shall direct the head of each Federal land management agency under the jurisdiction of the Secretary concerned\u2014\n**(1)**\nto establish a new categorical exclusion from the requirements of title I of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4331 et seq. ) for projects involving an existing communications facility that would improve public safety on Federal land, such as\u2014\n**(A)**\nproviding backup power for the communications facility;\n**(B)**\nimproving supporting infrastructure at the communications facility; or\n**(C)**\nproviding more reliable or redundant connection capabilities using the communications facility; or\n**(2)**\nto adopt an existing categorical exclusion from another agency under section 109 of that Act ( 42 U.S.C. 4336c ) applicable to projects described in paragraph (1).\n#### 7. Previously analyzed Federal land\n##### (a) Nonapplicability of certain review requirements\nThe review requirements of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) and division A of subtitle III of title 54, United States Code, shall not apply to an application for a communications use authorization on Federal land (including Federal land on which authorized utilities, communications facilities, powerline facilities, or roads have been installed), if\u2014\n**(1)**\nthe communications equipment is located in or on existing infrastructure; or\n**(2)**\nthe communications facility is located on previously analyzed Federal land.\n##### (b) No additional consultation required under certain circumstances\nNotwithstanding any other provision of law, the Secretary concerned shall not be required to reinitiate consultation under the requirements of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) or division A of subtitle III of title 54, United States Code, for an application for a communications use authorization on previously analyzed Federal land, regardless of whether new information concerning the previously analyzed Federal land becomes available.\n#### 8. Wireless facility modifications\nSection 6409(a) of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1455(a) ) is amended by striking paragraph (3).\n#### 9. Establishment of online portals\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, each Federal land management agency shall establish an online portal to accept an electronic SF\u2013299.\n##### (b) Coordination\nThe Federal land management agencies shall coordinate with each other to establish uniform versions of the online portal required under subsection (a).\n#### 10. Collection and retention of cost recovery fees\n##### (a) Collection and retention of cost recovery fees associated with communications use authorizations on Federal land and Federal land management agency support for communications site programs\n**(1) Special account required**\nThe Secretary of the Treasury shall establish a special account in the Treasury for each Federal land management agency for the deposit of cost recovery fees received by the Federal land management agency relating to communications use authorizations granted, issued, or executed by the Federal land management agency.\n**(2) Requirements for cost recovery fees**\nNotwithstanding any other provision of law, any cost recovery fees collected by a Federal land management agency pursuant to this section shall be\u2014\n**(A)**\ncollected only to the extent provided in advance in an appropriations Act;\n**(B)**\ncalculated and assessed on an annual basis;\n**(C)**\nbased solely on costs incurred by organizational units in processing applications for communications use authorizations and overseeing any applicable construction activities relating to the communications use authorizations; and\n**(D)**\nimposed on a competitively neutral, technology-neutral, and nondiscriminatory basis with respect to other uses of the applicable communications site.\n**(3) Deposit and retention of cost recovery fees**\nCost recovery fees received by a Federal land management agency shall\u2014\n**(A)**\nbe deposited in the special account established for that Federal land management agency under paragraph (1); and\n**(B)**\nremain available for expenditure under paragraph (4), to the extent and in such amounts as are provided in advance in appropriations Acts.\n**(4) Expenditure of retained fees**\nAmounts deposited in the special account established for a Federal land management agency under paragraph (1) shall be used by the Federal land management agency for activities relating to communications use authorizations or communications sites, including the following:\n**(A)**\nAdministering communications use authorizations, including through cooperative agreements under subsection (b).\n**(B)**\nPreparing needs assessments or other programmatic analyses necessary to establish communications sites and authorize communications uses on or adjacent to Federal land.\n**(C)**\nDeveloping management plans for the placement of communications sites on or adjacent to Federal land on a competitively neutral, technology-neutral, nondiscriminatory basis.\n**(D)**\nTraining for management of communications sites on or adjacent to Federal land.\n**(E)**\nObtaining, improving access to, or establishing communications sites on or adjacent to Federal land.\n**(F)**\nHiring and training personnel to perform duties that will help\u2014\n**(i)**\nto streamline permitting processes associated with communications use authorizations and the use of communications sites for communications use on Federal land; and\n**(ii)**\nto reduce the time it takes for permits relating to communications use authorizations and the use of communications sites for communications use on Federal land to be approved.\n**(5) No effect on other fee retention authorities**\nThis subsection shall not limit or otherwise affect fee retention by a Federal land management agency under any other authority.\n##### (b) Cooperative agreement authority\nThe Secretary of the Interior may enter into cooperative agreements to carry out the activities described in subsection (a)(4).\n#### 11. Federal Land Management Agency Working Group\n##### (a) Establishment\nThere is established a working group, to be known as the Federal Land Management Agency Working Group .\n##### (b) Membership\nThe working group shall be composed of 1 representative of each of the Federal land management agencies, to be appointed by the Secretary concerned.\n##### (c) Duties\nThe working group shall\u2014\n**(1)**\nperiodically meet to coordinate and expedite the review of applications for communications use authorizations; and\n**(2)**\ncoordinate with the Federal Communications Commission to use broadband location data created under section 802(c) of the Communications Act of 1934 ( 47 U.S.C. 642(c) ) to identify unserved locations that may need to use a Federal right-of-way and prepare for potential communications use authorization applications.",
      "versionDate": "2026-05-19",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4561is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "CLOSE THE GAP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-29T07:23:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CLOSE THE GAP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-29T07:23:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Closing Long Overdue Streamlining Encumbrances To Help Expeditiously Generate Approved Permits Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-29T07:23:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to modernize and streamline the permitting process for broadband infrastructure on Federal land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-29T07:18:37Z"
    }
  ]
}
```
