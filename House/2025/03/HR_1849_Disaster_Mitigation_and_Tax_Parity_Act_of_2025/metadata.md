# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1849?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1849
- Title: Disaster Mitigation and Tax Parity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1849
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-05-20T08:08:42Z
- Update date including text: 2026-05-20T08:08:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-02-04 16:15:37 - Floor: ASSUMING FIRST SPONSORSHIP - Mr. Murphy asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1849, a bill originally introduced by Representative LaMalfa, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-02-04 16:15:37 - Floor: ASSUMING FIRST SPONSORSHIP - Mr. Murphy asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1849, a bill originally introduced by Representative LaMalfa, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1849",
    "number": "1849",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000578",
        "district": "1",
        "firstName": "Doug",
        "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
        "lastName": "LaMalfa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Disaster Mitigation and Tax Parity Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:42Z",
    "updateDateIncludingText": "2026-05-20T08:08:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H8D000",
      "actionDate": "2026-02-04",
      "actionTime": "16:15:37",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "ASSUMING FIRST SPONSORSHIP - Mr. Murphy asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1849, a bill originally introduced by Representative LaMalfa, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-03-05T15:06:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "NC"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "NC"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "WI"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CO"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "LA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "AL"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NC"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "CA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "AL"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "AL"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "CA"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "NC"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "NC"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NC"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1849ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1849\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. LaMalfa (for himself, Mr. Thompson of California , Mr. Murphy , Ms. Brownley , Mr. Rouzer , Mr. Davis of Illinois , Mr. Fitzgerald , Ms. Pettersen , Mr. Higgins of Louisiana , Mr. Peters , Mr. Mullin , Ms. Chu , Ms. Sewell , and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide for the exclusion from gross income of amounts received from State-based catastrophe loss mitigation programs.\n#### 1. Short title\nThis Act may be cited as the Disaster Mitigation and Tax Parity Act of 2025 .\n#### 2. Exclusion of amounts received from State-based catastrophe loss mitigation programs\n##### (a) In general\nSection 139 of the Internal Revenue Code of 1986 is amended by redesignating subsection (h) as subsection (i) and by inserting after subsection (g) the following new subsection:\n(h) State-Based catastrophe loss mitigation programs (1) In general Gross income shall not include any amount received by or paid for the benefit of an individual as a qualified catastrophe mitigation payment under a program established by\u2014 (A) a State or any political subdivision or public instrumentality thereof, (B) a joint powers authority, or (C) an entity created by State law to ensure the availability of an adequate market of last resort for essential property insurance or basic property insurance, over which a State agency or State department of insurance has regulatory oversight, for the purpose of making such payments. (2) Qualified catastrophe mitigation payment For purposes of this section, the term qualified catastrophe mitigation payment means any amount which is received by or paid for the benefit of the owner of any property to make improvements to such property for the sole purpose of reducing the damage that would be done to such property by a windstorm, earthquake, or wildfire. (3) No increase in basis Rules similar to the rules of subsection (g)(3) shall apply in the case of this subsection. .\n##### (b) Conforming amendments\n**(1)**\nSection 139(d) of the Internal Revenue Code of 1986 is amended by striking and qualified and inserting , qualified catastrophe mitigation payments, and qualified .\n**(2)**\nSection 139(i) of such Code (as redesignated by subsection (a)) is amended by striking or qualified and inserting , qualified catastrophe mitigation payment, or qualified .\n##### (c) Effective date\n**(1) In general**\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2020.\n**(2) Retroactive applicability**\nThe Secretary of the Treasury, or the Secretary\u2019s delegate, shall provide an opportunity for individuals to claim the exclusion from gross income under section 139(h) of the Internal Revenue Code of 1986, as added by this section, including by amended return.",
      "versionDate": "2025-03-05",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-30",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "336",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Disaster Mitigation and Tax Parity Act of 2025",
      "type": "S"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Disaster relief and insurance",
            "updateDate": "2026-02-06T18:10:14Z"
          },
          {
            "name": "Income tax exclusion",
            "updateDate": "2026-02-06T18:10:14Z"
          },
          {
            "name": "Natural disasters",
            "updateDate": "2026-02-06T18:10:14Z"
          },
          {
            "name": "Residential rehabilitation and home repair",
            "updateDate": "2026-02-06T18:10:14Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-02-06T18:10:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-05-07T19:53:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1849",
          "measure-number": "1849",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-05",
          "originChamber": "HOUSE",
          "update-date": "2025-07-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1849v00",
            "update-date": "2025-07-09"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Disaster Mitigation and Tax Parity Act of 2025</strong></p><p>This bill excludes from gross income, for federal income tax purposes, payments received from a state catastrophe loss mitigation program by an individual\u00a0for the purpose of making improvements to the individual\u2019s property that mitigate the impact of certain disasters.</p><p>Under current law, individuals may exclude from gross income, for federal income tax purposes, payments received under the Robert\u00a0T. Stafford Disaster Relief and Emergency Assistance Act or the National Flood Insurance Act (as in effect on April 15, 2005) for hazard mitigation. (Some exceptions apply.) Further, under current law, such payments do not increase the basis of the property for which the payments are made.</p><p>The bill allows a similar exclusion from gross income for certain payments received by an individual from a program established by</p><ul><li>a state (or any political subdivision or instrumentality of the state),</li><li>a joint powers authority, or</li><li>an entity that was established by the state to provide essential or basic property insurance and is regulated by the state.</li></ul><p>Under the bill, such payments must be for making improvements to the individual\u2019s property for the sole purpose of reducing damage that would be done to the property by a windstorm, earthquake, flood, or wildfire.</p><p>Finally, the bill provides that such payments from a state catastrophe loss mitigation program do not increase the basis of the property for which the payments are made.</p>"
        },
        "title": "Disaster Mitigation and Tax Parity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1849.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disaster Mitigation and Tax Parity Act of 2025</strong></p><p>This bill excludes from gross income, for federal income tax purposes, payments received from a state catastrophe loss mitigation program by an individual\u00a0for the purpose of making improvements to the individual\u2019s property that mitigate the impact of certain disasters.</p><p>Under current law, individuals may exclude from gross income, for federal income tax purposes, payments received under the Robert\u00a0T. Stafford Disaster Relief and Emergency Assistance Act or the National Flood Insurance Act (as in effect on April 15, 2005) for hazard mitigation. (Some exceptions apply.) Further, under current law, such payments do not increase the basis of the property for which the payments are made.</p><p>The bill allows a similar exclusion from gross income for certain payments received by an individual from a program established by</p><ul><li>a state (or any political subdivision or instrumentality of the state),</li><li>a joint powers authority, or</li><li>an entity that was established by the state to provide essential or basic property insurance and is regulated by the state.</li></ul><p>Under the bill, such payments must be for making improvements to the individual\u2019s property for the sole purpose of reducing damage that would be done to the property by a windstorm, earthquake, flood, or wildfire.</p><p>Finally, the bill provides that such payments from a state catastrophe loss mitigation program do not increase the basis of the property for which the payments are made.</p>",
      "updateDate": "2025-07-09",
      "versionCode": "id119hr1849"
    },
    "title": "Disaster Mitigation and Tax Parity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disaster Mitigation and Tax Parity Act of 2025</strong></p><p>This bill excludes from gross income, for federal income tax purposes, payments received from a state catastrophe loss mitigation program by an individual\u00a0for the purpose of making improvements to the individual\u2019s property that mitigate the impact of certain disasters.</p><p>Under current law, individuals may exclude from gross income, for federal income tax purposes, payments received under the Robert\u00a0T. Stafford Disaster Relief and Emergency Assistance Act or the National Flood Insurance Act (as in effect on April 15, 2005) for hazard mitigation. (Some exceptions apply.) Further, under current law, such payments do not increase the basis of the property for which the payments are made.</p><p>The bill allows a similar exclusion from gross income for certain payments received by an individual from a program established by</p><ul><li>a state (or any political subdivision or instrumentality of the state),</li><li>a joint powers authority, or</li><li>an entity that was established by the state to provide essential or basic property insurance and is regulated by the state.</li></ul><p>Under the bill, such payments must be for making improvements to the individual\u2019s property for the sole purpose of reducing damage that would be done to the property by a windstorm, earthquake, flood, or wildfire.</p><p>Finally, the bill provides that such payments from a state catastrophe loss mitigation program do not increase the basis of the property for which the payments are made.</p>",
      "updateDate": "2025-07-09",
      "versionCode": "id119hr1849"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1849ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Disaster Mitigation and Tax Parity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disaster Mitigation and Tax Parity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide for the exclusion from gross income of amounts received from State-based catastrophe loss mitigation programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:06Z"
    }
  ]
}
```
