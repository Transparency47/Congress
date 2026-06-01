# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2077?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2077
- Title: Expanded Coverage for Former Foster Youth Act
- Congress: 119
- Bill type: S
- Bill number: 2077
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2025-07-25T16:22:30Z
- Update date including text: 2025-07-25T16:22:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2077",
    "number": "2077",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "Expanded Coverage for Former Foster Youth Act",
    "type": "S",
    "updateDate": "2025-07-25T16:22:30Z",
    "updateDateIncludingText": "2025-07-25T16:22:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T19:27:55Z",
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MD"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NM"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "OR"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NV"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2077is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2077\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mr. Welch (for himself, Ms. Alsobrooks , Ms. Klobuchar , Mr. Luj\u00e1n , Mr. Wyden , and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XIX of the Social Security Act to ensure health insurance coverage continuity for former foster youth.\n#### 1. Short title\nThis Act may be cited as the Expanded Coverage for Former Foster Youth Act .\n#### 2. Coverage continuity for former foster care children up to age 26\n##### (a) In general\nSection 1902(a)(10)(A)(i)(IX) of the Social Security Act ( 42 U.S.C. 1396a(a)(10)(A)(i)(IX) ) is amended to read as follows:\n(IX) who\u2014 (aa) are under 26 years of age; (bb) are not described in and are not enrolled under any of subclauses (I) through (VII) of this clause or are described in any of such subclauses but have income that exceeds the level of income applicable under the State plan for eligibility to enroll for medical assistance under such subclause; and (cc) were in foster care under the responsibility of a State on the date of attaining 18 years of age (or such higher age as such State has elected under section 475(8)(B)(iii)), or were in such care at any age but subsequently left such care to enter into a legal guardianship with a kinship caregiver (without regard to whether kinship guardianship payments are being made on behalf of the child under this part), or were emancipated from such care prior to attaining age 18; .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on January 1, 2026, and shall apply with respect to individuals who attain 18 years of age on or after that date.\n#### 3. Outreach efforts for enrollment of former foster children\nSection 1902(a) of the Social Security Act ( 42 U.S.C. 1396a(a) ) is amended\u2014\n**(1)**\nin paragraph (86), by striking ; and and inserting a semicolon;\n**(2)**\nin paragraph (87)(D), by striking the period at the end and inserting ; and ; and\n**(3)**\nby inserting after paragraph (87)(D) the following new paragraph:\n(88) not later than January 1, 2026, establish an outreach and enrollment program, in coordination with the State agency responsible for administering the State plan under part E of title IV and any other appropriate or interested agencies, designed to increase the enrollment of individuals who are eligible for medical assistance under the State plan under paragraph (10)(A)(i)(IX) in accordance with best practices established by the Secretary. .",
      "versionDate": "2025-06-12",
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
        "name": "Health",
        "updateDate": "2025-07-08T13:24:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-12",
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
          "measure-id": "id119s2077",
          "measure-number": "2077",
          "measure-type": "s",
          "orig-publish-date": "2025-06-12",
          "originChamber": "SENATE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2077v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-06-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Expanded Coverage for Former Foster Youth Act</strong></p><p>This bill modifies provisions relating to the coverage of former foster youths under Medicaid.</p><p>Under current law, a state Medicaid program must cover former foster youths until the age of 26 if the youths were in a state's foster care system at the age of 18 and were enrolled in a state's Medicaid program while in foster care. The bill requires state Medicaid programs to also cover former foster youths who were placed in a legal guardianship with a kinship caregiver or were emancipated from foster care before the age of 18. The bill repeals the provision that requires former foster youths to have been enrolled in a state Medicaid program while in foster care in order to qualify for Medicaid coverage until the age of 26.</p><p>The bill also requires states to establish Medicaid outreach and enrollment programs for former foster youths.</p>"
        },
        "title": "Expanded Coverage for Former Foster Youth Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2077.xml",
    "summary": {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Expanded Coverage for Former Foster Youth Act</strong></p><p>This bill modifies provisions relating to the coverage of former foster youths under Medicaid.</p><p>Under current law, a state Medicaid program must cover former foster youths until the age of 26 if the youths were in a state's foster care system at the age of 18 and were enrolled in a state's Medicaid program while in foster care. The bill requires state Medicaid programs to also cover former foster youths who were placed in a legal guardianship with a kinship caregiver or were emancipated from foster care before the age of 18. The bill repeals the provision that requires former foster youths to have been enrolled in a state Medicaid program while in foster care in order to qualify for Medicaid coverage until the age of 26.</p><p>The bill also requires states to establish Medicaid outreach and enrollment programs for former foster youths.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s2077"
    },
    "title": "Expanded Coverage for Former Foster Youth Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Expanded Coverage for Former Foster Youth Act</strong></p><p>This bill modifies provisions relating to the coverage of former foster youths under Medicaid.</p><p>Under current law, a state Medicaid program must cover former foster youths until the age of 26 if the youths were in a state's foster care system at the age of 18 and were enrolled in a state's Medicaid program while in foster care. The bill requires state Medicaid programs to also cover former foster youths who were placed in a legal guardianship with a kinship caregiver or were emancipated from foster care before the age of 18. The bill repeals the provision that requires former foster youths to have been enrolled in a state Medicaid program while in foster care in order to qualify for Medicaid coverage until the age of 26.</p><p>The bill also requires states to establish Medicaid outreach and enrollment programs for former foster youths.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s2077"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2077is.xml"
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
      "title": "Expanded Coverage for Former Foster Youth Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-26T06:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Expanded Coverage for Former Foster Youth Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T06:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XIX of the Social Security Act to ensure health insurance coverage continuity for former foster youth.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T06:48:22Z"
    }
  ]
}
```
