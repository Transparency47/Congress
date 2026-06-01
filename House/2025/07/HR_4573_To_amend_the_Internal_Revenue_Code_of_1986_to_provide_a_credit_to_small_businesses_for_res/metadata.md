# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4573?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4573
- Title: Innovate to Save Lives Act
- Congress: 119
- Bill type: HR
- Bill number: 4573
- Origin chamber: House
- Introduced date: 2025-07-21
- Update date: 2025-08-01T16:42:52Z
- Update date including text: 2025-08-01T16:42:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-21: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-07-21: Introduced in House

## Actions

- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4573",
    "number": "4573",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Innovate to Save Lives Act",
    "type": "HR",
    "updateDate": "2025-08-01T16:42:52Z",
    "updateDateIncludingText": "2025-08-01T16:42:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-21",
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
      "actionDate": "2025-07-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-21",
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
          "date": "2025-07-21T16:01:45Z",
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
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "AZ"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "NE"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "OR"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4573ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4573\nIN THE HOUSE OF REPRESENTATIVES\nJuly 21, 2025 Mr. Neguse (for himself, Mr. Ciscomani , Ms. Dean of Pennsylvania , Mr. Bacon , Ms. Dexter , and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a credit to small businesses for research activities related to the mitigation of certain drug threats.\n#### 1. Short title\nThis Act may be cited as the Innovate to Save Lives Act .\n#### 2. Credit for research activities of small businesses related to the mitigation of certain drug threats\n##### (a) In general\nSection 41(a) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (2), by striking the period at the end of paragraph (3) and inserting , and , and by adding at the end the following new paragraph:\n(4) in the case of a small business (as defined in subsection (b)(3)(D)(iii)), 10 percent of the qualified drug threat mitigation research expenses (as defined in subsection (i)) for the taxable year. .\n##### (b) Definitions\nSection 41 of such Code is amended by adding at the end the following new subsection:\n(i) Qualified drug threat mitigation research expenses For purposes of this section\u2014 (1) Qualified drug threat mitigation research expenses The term qualified drug threat mitigation research expenses means the qualified research expenses which would be determined under subsection (b) if qualified drug threat mitigation research were substituted for qualified research each place it appears therein. (2) Qualified drug threat mitigation research The term qualified drug threat mitigation research means qualified research which is undertaken for the purpose of discovering information related to mitigating or treating the effects of the use of a specified drug or to preventing, diverting, or intervening in such use. Such term shall not include any clinical research unless such research complies with the policies and guidelines of the National Institutes of Health for clinical research. (3) Specified drug (A) In general The term specified drug means any emerging drug, fentanyl, fentanyl-related substance, or methamphetamine. (B) Emerging drug The term emerging drug means a drug designated as an emerging drug threat under section 709(c) of the Office of National Drug Control Policy Reauthorization Act of 1998 ( 21 U.S.C. 1708(c) ). Such term shall include any such drug for any taxable year if such designation is in effect under such section at any time during such taxable year. (C) Fentanyl-related substance The term fentanyl-related substance means any substance that is structurally related to fentanyl by 1 or more of the following modifications: (i) By replacement of the phenyl portion of the phenethyl group by any monocycle, whether or not further substituted in or on the monocycle. (ii) By substitution in or on the phenethyl group with alkyl, alkenyl, alkoxyl, hydroxyl, halo, haloalkyl, amino, or nitro groups. (iii) By substitution in or on the piperidine ring with alkyl, alkenyl, alkoxyl, ester, ether, hydroxyl, halo, haloalkyl, amino, or nitro groups. (iv) By replacement of the aniline ring with any aromatic monocycle whether or not further substituted in or on the aromatic monocycle. (v) By replacement of the N\u2013propionyl group with another acyl group. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n##### (d) GAO report\n5 years after the date of the enactment of this Act, the Comptroller General shall submit a written report to Congress regarding the amount of tax credits allowed under section 41(a)(4) of the Internal Revenue Code of 1986 for qualified drug threat mitigation expenses and the types of qualified drug threat mitigation research with respect to which such credits were allowed. The Comptroller General shall ensure that the data in such report is anonymous and that any studies undertaken to prepare such report do not impede qualified drug threat mitigation research.",
      "versionDate": "2025-07-21",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-08-01T16:42:52Z"
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
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4573ih.xml"
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
      "title": "Innovate to Save Lives Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T09:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Innovate to Save Lives Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T09:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide a credit to small businesses for research activities related to the mitigation of certain drug threats.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T09:33:16Z"
    }
  ]
}
```
