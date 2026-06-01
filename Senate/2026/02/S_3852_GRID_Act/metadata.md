# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3852?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3852
- Title: GRID Act
- Congress: 119
- Bill type: S
- Bill number: 3852
- Origin chamber: Senate
- Introduced date: 2026-02-11
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in Senate
- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2026-02-11: Introduced in Senate

## Actions

- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3852",
    "number": "3852",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "GRID Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-11",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T22:33:50Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3852is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3852\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2026 Mr. Hawley (for himself and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo impose certain requirements on data centers to ensure the prioritization of residential ratepayers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guaranteeing Rate Insulation from Data Centers Act or the GRID Act .\n#### 2. Findings\nCongress finds that the construction and operation of data centers and the power sources used to supply data centers with energy\u2014\n**(1)**\nare matters concerning interstate commerce, including the channels of interstate commerce, the instrumentalities of interstate commerce, and persons and things in interstate commerce; and\n**(2)**\nconstitute economic activities that have a substantial effect on interstate commerce.\n#### 3. Definitions\nIn this Act:\n**(1) Covered entity**\nThe term covered entity means a private company, or other private entity, that\u2014\n**(A)**\nowns, operates, or maintains a data center; or\n**(B)**\nhas plans to own, operate, or maintain a data center within the next 5 years.\n**(2) Data center**\nThe term data center means a data center (as defined in section 453(a) of the Energy Independence and Security Act of 2007 ( 42 U.S.C. 17112(a) )) with a power demand of 20 megawatts or more that is not owned, operated, or maintained\u2014\n**(A)**\nby a covered agency (as defined in section 834(a) of the Carl Levin and Howard P. Buck McKeon National Defense Authorization Act for Fiscal Year 2015 ( Public Law 113\u2013291 ; 44 U.S.C. 3601 note)); or\n**(B)**\nby a contractor on behalf of a covered agency (as so defined).\n**(3) Electric utility**\nThe term electric utility has the meaning given the term in section 3 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2602 ).\n**(4) Existing data center**\nThe term existing data center means a data center that has already begun operations.\n**(5) New data center**\nThe term new data center means a data center or planned data center that is not yet operational.\n**(6) Rate Effect Credit**\nThe term Rate Effect Credit means a credit paid by a covered entity to an appropriate party, as determined by the Secretary, that offsets the effect that a data center would otherwise have on the electrical rates paid by ratepayers.\n**(7) Secretary**\nThe term Secretary means the Secretary of Energy.\n**(8) Utility**\nThe term utility includes, as the Secretary determines to be appropriate\u2014\n**(A)**\nan electric utility;\n**(B)**\na gas utility (as defined in section 302 of the Public Utility Regulatory Policies Act of 1978 ( 15 U.S.C. 3202 ));\n**(C)**\na public water system (as defined in section 1401 of the Safe Drinking Water Act ( 42 U.S.C. 300f ));\n**(D)**\na treatment works (as defined in section 212 of the Federal Water Pollution Control Act ( 33 U.S.C. 1292 )); and\n**(E)**\nany other regulated utility that provides water, energy, or other essential services to a data center.\n**(9) Zero Rate Effect Certificate**\nThe term Zero Rate Effect Certificate means a certificate issued by the Secretary under section 4(b).\n#### 4. Data center requirement for off-grid power supply\n##### (a) Prohibition\n**(1) In general**\nSubject to paragraph (2), beginning on the date that is 180 days after the date of enactment of this Act, a covered entity may not build, own, operate, or maintain a data center unless the data center derives all of its energy, including back-up energy, from a captive power plant, on-site power generation, or some other source or combination of sources separate from, and not deriving power from, the electric grid.\n**(2) Existing data centers**\nUntil the date that is 10 years after the date of enactment of this Act, a covered entity that owns, operates, or maintains an existing data center that derives any of its energy from the electric grid as of the date described in paragraph (1) may comply with the prohibition under that paragraph by obtaining and maintaining an unexpired Zero Rate Effect Certificate.\n##### (b) Zero rate effect certificate\n**(1) In general**\nFor the 10-year period beginning on the date of enactment of this Act, a covered entity that owns, operates, or maintains an existing data center that derives any of its energy from the electric grid shall submit to the Secretary a request for the issuance of a Zero Rate Effect Certificate for that data center.\n**(2) Study required**\nOn receipt of a request for a Zero Rate Effect Certificate, the Secretary shall study and determine\u2014\n**(A)**\nhow interconnection costs and other infrastructure costs needed to supply the data center with power from the electric grid are allocated;\n**(B)**\nthe contribution of the data center to coincident peak, including load factors, and any effects on capacity charges;\n**(C)**\nthe effects on the locational marginal price for\u2014\n**(i)**\nthe local electric grid; and\n**(ii)**\nthe relevant region;\n**(D)**\nany changes in value-cost ratios;\n**(E)**\nany effects on the marginal cost of generation;\n**(F)**\nany changes in line loss percentages caused by heavier loads on local distribution lines;\n**(G)**\nany offsets in data center power infrastructure cost-sharing by ratepayers through Rate Effect Credits or other financial arrangements described in subsection (c); and\n**(H)**\nany other metrics or information the Secretary determines relevant.\n**(3) Issuance of certificate**\n**(A) In general**\nIf the Secretary determines, based on the study conducted under paragraph (2), that the relevant data center will not increase the electrical rates paid by ratepayers, the Secretary shall issue a Zero Rate Effect Certificate for the data center.\n**(B) Residential ratepayer prioritization**\nIn making a determination under subparagraph (A), the Secretary shall prioritize the electrical rates paid by residential ratepayers over all other ratepayer classes.\n**(4) Duration of certificate**\nA Zero Rate Effect Certificate issued under paragraph (3) shall expire 1 year after the date of issuance.\n**(5) Reissuance**\nA covered entity may apply for the reissuance of a Zero Rate Effect Certificate as necessary.\n##### (c) Rate Effect Credits\n**(1) In general**\nA covered entity may meet the requirements for the issuance of a Zero Rate Effect Certificate by paying Rate Effect Credits or through some other financial arrangement that, in the determination of the Secretary, would offset the effect on the electrical rates paid by ratepayers.\n**(2) Residential ratepayer prioritization**\nIn making a determination under paragraph (1), the Secretary shall prioritize the electrical rates paid by residential ratepayers over all other ratepayer classes.\n##### (d) Legal requirement\nAny power source, including a captive power plant, on-site generation, or other source described in subsection (a)(1), that is used to generate electricity for a data center shall comply with all applicable local, State, and Federal laws (including regulations) based on the actual use and emissions of the power source.\n##### (e) Labor requirement\nA covered entity seeking to construct any power source described in subsection (a)(1) shall enter into a project labor agreement (as defined in section 52.222\u201334(a) of title 48, Code of Federal Regulations (or a successor regulation)) for the construction of the power source.\n##### (f) Enforcement\nAny person who violates subsection (a) shall be subject to a civil penalty of not less than $1,000,000 per day of the violation.\n##### (g) Regulations\n**(1) In general**\nThe Secretary may promulgate such regulations as the Secretary determines to be necessary to implement this section.\n**(2) Residential ratepayer prioritization**\nIn promulgating regulations under paragraph (1), the Secretary shall prioritize the electrical rates paid by residential ratepayers over all other ratepayer classes.\n#### 5. Data center reporting requirements\n##### (a) Utility usage\nNot later than 90 days after the date of enactment of this Act, the Secretary shall establish a national requirement for covered entities to provide to the public\u2014\n**(1)**\nfor each new data center that is, or is planned to be, owned, operated, or maintained by the covered entity, estimates of the utility usage by the new data center for\u2014\n**(A)**\nthe first year of planned operation of the new data center; and\n**(B)**\neach of the next 5 years following that first year of planned operation; and\n**(2)**\nfor each existing data center that is, or is planned to be, owned, operated, or maintained by the covered entity\u2014\n**(A)**\nestimates of the utility usage by the existing data center for\u2014\n**(i)**\nthe current year; and\n**(ii)**\neach of the next 5 years; and\n**(B)**\ninformation on the actual utility usage during each of the 5 most recent previous years during which the existing data center was operational.\n##### (b) Real property or possessory interests\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, the Secretary shall establish a national requirement for covered entities to publicly disclose any acquisition of real property or a possessory interest in real property (including a lease) with the intent to build or expand a data center.\n**(2) Requirement**\nThe disclosure under paragraph (1) shall include\u2014\n**(A)**\nany transaction or agreement relating to the acquisition described in that paragraph between\u2014\n**(i)**\nthe covered entity; and\n**(ii)**\nany party from which the real property or possessory interest is acquired;\n**(B)**\nany related transaction or agreement between the covered entity and any government entity; and\n**(C)**\nany related transaction or agreement between a party described in subparagraph (A)(ii) and any government entity.\n##### (c) Agreements\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, the Secretary shall establish a national requirement for\u2014\n**(A)**\ncovered entities to publicly disclose any transaction or agreement with a utility regarding utility service for a data center, including any financial arrangement for a Rate Effect Credit; and\n**(B)**\nutilities to publicly disclose any transaction or agreement with a covered entity or a data center regarding utility service for a data center, including any financial arrangement for a Rate Effect Credit.\n**(2) Requirement**\nThe disclosure under paragraph (1) shall include\u2014\n**(A)**\na description of any subsidy, credit, discount, cost-sharing arrangement, tax benefit, or other incentive, financial or otherwise, that the utility, local government or municipality, or State government provides, or has agreed to provide, to the covered entity regarding utility service; and\n**(B)**\nwith respect to each subsidy, credit, discount, cost-sharing arrangement, tax benefit, or other incentive described in subparagraph (A)\u2014\n**(i)**\nan estimate of total savings for the covered entity; and\n**(ii)**\na statement of whether the covered entity is financially affiliated with the applicable utility.",
      "versionDate": "2026-02-11",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Energy",
        "updateDate": "2026-03-02T18:01:59Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3852is.xml"
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
      "title": "GRID Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GRID Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Guaranteeing Rate Insulation from Data Centers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to impose certain requirements on data centers to ensure the prioritization of residential ratepayers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T04:18:31Z"
    }
  ]
}
```
