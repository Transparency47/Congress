# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/336?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/336
- Title: Disaster Mitigation and Tax Parity Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 336
- Origin chamber: Senate
- Introduced date: 2025-01-30
- Update date: 2025-12-10T06:45:34Z
- Update date including text: 2025-12-10T06:45:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-30: Introduced in Senate
- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-30: Introduced in Senate

## Actions

- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-30",
    "latestAction": {
      "actionDate": "2025-01-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/336",
    "number": "336",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Disaster Mitigation and Tax Parity Act of 2025",
    "type": "S",
    "updateDate": "2025-12-10T06:45:34Z",
    "updateDateIncludingText": "2025-12-10T06:45:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-30",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-30",
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
          "date": "2025-01-30T19:34:19Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "CA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "LA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "CA"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "LA"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "CO"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "NC"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "MN"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "MS"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "CO"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "OR"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "AL"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s336is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 336\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Mr. Tillis (for himself, Mr. Padilla , Mr. Cassidy , Mr. Schiff , Mr. Kennedy , Mr. Hickenlooper , Mr. Budd , Ms. Klobuchar , Mr. Wicker , Mr. Bennet , and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude from gross income amounts received from State-based catastrophe loss mitigation programs.\n#### 1. Short title\nThis Act may be cited as the Disaster Mitigation and Tax Parity Act of 2025 .\n#### 2. Exclusion of amounts received from State-based catastrophe loss mitigation programs\n##### (a) In general\nSection 139 of the Internal Revenue Code of 1986 is amended by redesignating subsection (h) as subsection (i) and by inserting after subsection (g) the following new subsection:\n(h) State-Based catastrophe loss mitigation programs (1) In general Gross income shall not include any amount received by or paid for the benefit of an individual as a qualified catastrophe mitigation payment under a program established by\u2014 (A) a State or any political subdivision or public instrumentality thereof, (B) a joint powers authority, or (C) an entity created by State law to ensure the availability of an adequate market of last resort for essential property insurance or basic property insurance, over which a State agency or State department of insurance has regulatory oversight, for the purpose of making such payments. (2) Qualified catastrophe mitigation payment For purposes of this section, the term qualified catastrophe mitigation payment means any amount (other than the amount of any qualified disaster mitigation payment) which is received by or paid for the benefit of the owner of any property to make improvements to such property for the sole purpose of reducing the damage that would be done to such property by a windstorm, earthquake, flood, or wildfire. (3) No increase in basis Rules similar to the rules of subsection (g)(3) shall apply in the case of this subsection. .\n##### (b) Conforming amendments\n**(1)**\nSection 139(d) of the Internal Revenue Code of 1986 is amended by striking and qualified and inserting , qualified catastrophe mitigation payments, and qualified .\n**(2)**\nSection 139(i) of such Code (as redesignated by subsection (a)) is amended by striking or qualified and inserting , qualified catastrophe mitigation payment, or qualified .\n##### (c) Effective date\n**(1) In general**\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2021.\n**(2) Retroactive applicability**\nThe Secretary of the Treasury, or the Secretary's delegate, shall provide an opportunity for individuals to claim the exclusion from gross income under section 139(h) of the Internal Revenue Code of 1986, as added by this section, including by amended return.",
      "versionDate": "2025-01-30",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-03-05",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1849",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Disaster Mitigation and Tax Parity Act of 2025",
      "type": "HR"
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
        "name": "Taxation",
        "updateDate": "2025-04-28T21:57:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-30",
    "originChamber": "Senate",
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
          "measure-id": "id119s336",
          "measure-number": "336",
          "measure-type": "s",
          "orig-publish-date": "2025-01-30",
          "originChamber": "SENATE",
          "update-date": "2025-06-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s336v00",
            "update-date": "2025-06-24"
          },
          "action-date": "2025-01-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Disaster Mitigation and Tax Parity Act of 2025</strong></p><p>This bill excludes from gross income, for federal income tax purposes, payments received from a state catastrophe loss mitigation program by an individual\u00a0for the purpose of making improvements to the individual\u2019s property that mitigate the impact of certain disasters.</p><p>Under current law, individuals may exclude from gross income, for federal income tax purposes, payments received under the Robert\u00a0T. Stafford Disaster Relief and Emergency Assistance Act or the National Flood Insurance Act (as in effect on April 15, 2005) for hazard mitigation. (Some exceptions apply.) Further, under current law, such payments do not increase the basis of the property for which the payments are made.</p><p>The bill allows a similar exclusion from gross income for certain payments received by an individual from a program established by</p><ul><li>a state (or any political subdivision or instrumentality of the state),</li><li>a joint powers authority, or</li><li>an entity that was established by the state to provide essential or basic property insurance and is regulated by the state.</li></ul><p>Under the bill, such payments must be for making improvements to the individual\u2019s property for the sole purpose of reducing damage that would be done to the property by a windstorm, earthquake, flood, or wildfire.</p><p>Finally, the bill provides that such payments from a state catastrophe loss mitigation program do not increase the basis of the property for which the payments are made.</p>"
        },
        "title": "Disaster Mitigation and Tax Parity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s336.xml",
    "summary": {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Disaster Mitigation and Tax Parity Act of 2025</strong></p><p>This bill excludes from gross income, for federal income tax purposes, payments received from a state catastrophe loss mitigation program by an individual\u00a0for the purpose of making improvements to the individual\u2019s property that mitigate the impact of certain disasters.</p><p>Under current law, individuals may exclude from gross income, for federal income tax purposes, payments received under the Robert\u00a0T. Stafford Disaster Relief and Emergency Assistance Act or the National Flood Insurance Act (as in effect on April 15, 2005) for hazard mitigation. (Some exceptions apply.) Further, under current law, such payments do not increase the basis of the property for which the payments are made.</p><p>The bill allows a similar exclusion from gross income for certain payments received by an individual from a program established by</p><ul><li>a state (or any political subdivision or instrumentality of the state),</li><li>a joint powers authority, or</li><li>an entity that was established by the state to provide essential or basic property insurance and is regulated by the state.</li></ul><p>Under the bill, such payments must be for making improvements to the individual\u2019s property for the sole purpose of reducing damage that would be done to the property by a windstorm, earthquake, flood, or wildfire.</p><p>Finally, the bill provides that such payments from a state catastrophe loss mitigation program do not increase the basis of the property for which the payments are made.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119s336"
    },
    "title": "Disaster Mitigation and Tax Parity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Disaster Mitigation and Tax Parity Act of 2025</strong></p><p>This bill excludes from gross income, for federal income tax purposes, payments received from a state catastrophe loss mitigation program by an individual\u00a0for the purpose of making improvements to the individual\u2019s property that mitigate the impact of certain disasters.</p><p>Under current law, individuals may exclude from gross income, for federal income tax purposes, payments received under the Robert\u00a0T. Stafford Disaster Relief and Emergency Assistance Act or the National Flood Insurance Act (as in effect on April 15, 2005) for hazard mitigation. (Some exceptions apply.) Further, under current law, such payments do not increase the basis of the property for which the payments are made.</p><p>The bill allows a similar exclusion from gross income for certain payments received by an individual from a program established by</p><ul><li>a state (or any political subdivision or instrumentality of the state),</li><li>a joint powers authority, or</li><li>an entity that was established by the state to provide essential or basic property insurance and is regulated by the state.</li></ul><p>Under the bill, such payments must be for making improvements to the individual\u2019s property for the sole purpose of reducing damage that would be done to the property by a windstorm, earthquake, flood, or wildfire.</p><p>Finally, the bill provides that such payments from a state catastrophe loss mitigation program do not increase the basis of the property for which the payments are made.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119s336"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s336is.xml"
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
      "title": "Disaster Mitigation and Tax Parity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T12:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Disaster Mitigation and Tax Parity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude from gross income amounts received from State-based catastrophe loss mitigation programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:25Z"
    }
  ]
}
```
