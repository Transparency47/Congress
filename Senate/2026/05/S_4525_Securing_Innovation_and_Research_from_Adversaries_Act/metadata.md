# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4525?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4525
- Title: Securing Innovation and Research from Adversaries Act
- Congress: 119
- Bill type: S
- Bill number: 4525
- Origin chamber: Senate
- Introduced date: 2026-05-14
- Update date: 2026-05-28T20:56:12Z
- Update date including text: 2026-05-28T20:56:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-14: Introduced in Senate
- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-05-14: Introduced in Senate

## Actions

- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4525",
    "number": "4525",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Securing Innovation and Research from Adversaries Act",
    "type": "S",
    "updateDate": "2026-05-28T20:56:12Z",
    "updateDateIncludingText": "2026-05-28T20:56:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-14",
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
          "date": "2026-05-14T14:54:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4525is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4525\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2026 Mr. Banks introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit certain federally funded research collaborations with certain foreign entities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing Innovation and Research from Adversaries Act .\n#### 2. Prohibition on federally funded research relationships with certain foreign entities\n##### (a) Prohibition\nNo Federal funds awarded through a federally funded research award may be used by an individual or entity described in subsection (b) to enter into, support, or carry out any research collaboration with\u2014\n**(1)**\nan entity listed on a United States Government restricted entity list; or\n**(2)**\nan individual associated with such an entity.\n##### (b) Individual or entity described\nAn individual or entity described in this subsection is an individual or entity participating in, receiving, or performing work under a federally funded research award.\n##### (c) Guidance\nTo carry out this section, the Director of the Office of Science and Technology Policy, in consultation with the heads of relevant Federal research agencies, shall issue Government-wide implementation guidance to ensure standardized compliance requirements, definitions, and enforcement mechanisms.\n##### (d) Waiver Authority\n**(1) In general**\nThe head of a Federal agency may waive the prohibition under subsection (a), on a case-by-case basis, if such head determines\u2014\n**(A)**\nthe waiver is necessary to advance the national security interests of the United States; or\n**(B)**\nthe research collaboration under subsection (a) that is the subject of the waiver is essential for a clearly defined scientific, public health, or national security purpose that cannot reasonably be achieved without such collaboration.\n**(2) Report**\nNot later than 30 days after granting a waiver under paragraph (1), the head of the Federal agency who granted the waiver shall submit to Congress a written notification that includes the following:\n**(A)**\nThe identity of the individual or entity that is the subject of waiver.\n**(B)**\nThe justification for such waiver.\n**(C)**\nThe mitigation measures implemented to protect the national security interests of the United States, if applicable.\n##### (e) Definitions\nIn this section:\n**(1) Federally funded research award**\nThe term federally funded research award means a grant, contract, cooperative agreement, other Federal financial assistance (as defined in section 200.1 of title 2, Code of Federal Regulations), or other award issued under other transaction authority.\n**(2) National Laboratory**\nThe term National Laboratory has the meaning given such term in section 2 of the Energy Policy Act of 2005 ( 42 U.S.C. 15801 ).\n**(3) Research collaboration**\nThe term research collaboration means any activity conducted as part of a federally funded research award, including the following:\n**(A)**\nJoint research activities or projects.\n**(B)**\nCo-authorship of scholarly publications, technical reports, or research outputs.\n**(C)**\nData or processing sharing, material transfer, or exchange of research results, including access to datasets, software, or research infrastructure.\n**(D)**\nJoint laboratories, research centers, or institutes.\n**(E)**\nPersonnel exchanges, visiting scholar appointments, or joint supervision of students or researchers.\n**(F)**\nAny other arrangement determined by the head of the relevant Federal research funding agency to constitute research collaboration.\n**(4) United States Government restricted entity lists**\nThe term United States Government restricted entity list includes the following:\n**(A)**\nAny of the following lists maintained by the Bureau of Industry and Security of the Department of Commerce:\n**(i)**\nThe Entity List set forth in Supplement No. 4 to part 744 of title 15, Code of Federal Regulations.\n**(ii)**\nThe Unverified List set forth in Supplement No. 6 to part 744 of that title.\n**(iii)**\nThe Military End-User List set forth in Supplement No. 7 to part 744 of that title.\n**(iv)**\nThe Denied Persons List maintained pursuant to section 764.3(a)(2) of that title.\n**(B)**\nThe list of specially designated nationals and blocked persons maintained by the Office of Foreign Assets Control of the Department of the Treasury (commonly referred to as the SDN list ).\n**(C)**\nThe list of Chinese military companies operating in the United States required by section 1260H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ; 10 U.S.C. 113 note).\n**(D)**\nThe lists of debarred parties maintained by the Directorate of Defense Trade Controls of the Department of State pursuant to section 38(g)(4) of the Arms Export Control Act ( 22 U.S.C. 2778(g)(4) ).\n**(E)**\nThe list of telecommunications companies of the People\u2019s Republic of China described in section 889(f)(3) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ; 41 U.S.C. 3901 note prec.).\n**(F)**\nThe list of academic institutions of the People's Republic of China maintained under section 1286(c)(9)(A) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ; 10 U.S.C. 4001 note).\n**(G)**\nThe list of semiconductor companies of the People\u2019s Republic of China described in section 5949(j)(3) of the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 ( Public Law 117\u2013263 ; 41 U.S.C. 4713 note).\n**(H)**\nThe list of biotechnology companies of concern maintained under section 851(f) of the National Defense Authorization Act for Fiscal Year 2026 ( Public Law 119\u201360 ; 41 U.S.C. 3901 note prec.).\n**(I)**\nThe list of entities that produce or provide communications equipment or service on the list published by the Federal Communications Commission under section 2(a) of the Secure and Trusted Communications Networks Act of 2019 ( 47 U.S.C. 1601(a) ).\n**(J)**\nA list maintained under clause (i), (ii), (iv), or (v) of section 2(d)(2)(B) of the Act entitled An Act to ensure that goods made with forced labor in the Xinjiang Autonomous Region of the People\u2019s Republic of China do not enter the United States market, and for other purposes , approved December 23, 2021 ( Public Law 117\u201378 ; 22 U.S.C. 6901 note), (commonly referred to as the Uyghur Forced Labor Prevention Act ).\n**(K)**\nThe Annex to Executive Order 14032 ( 50 U.S.C. 1701 note; relating to addressing the threat from securities investments that finance certain companies of the People\u2019s Republic of China), or a successor order.\n**(L)**\nAny other list of entities designated by the President, the Secretary of Commerce, the Secretary of the Treasury, or the Secretary of Defense and with which transactions are restricted or prohibited for national security, foreign policy, or human rights reasons.",
      "versionDate": "2026-05-14",
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
        "name": "International Affairs",
        "updateDate": "2026-05-28T20:56:11Z"
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
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4525is.xml"
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
      "title": "Securing Innovation and Research from Adversaries Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T00:53:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Securing Innovation and Research from Adversaries Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-19T00:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit certain federally funded research collaborations with certain foreign entities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-19T00:48:41Z"
    }
  ]
}
```
