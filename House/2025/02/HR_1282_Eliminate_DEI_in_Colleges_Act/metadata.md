# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1282?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1282
- Title: Eliminate DEI in Colleges Act
- Congress: 119
- Bill type: HR
- Bill number: 1282
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-04-06T12:43:10Z
- Update date including text: 2026-04-06T12:43:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1282",
    "number": "1282",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001257",
        "district": "12",
        "firstName": "Gus",
        "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
        "lastName": "Bilirakis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Eliminate DEI in Colleges Act",
    "type": "HR",
    "updateDate": "2026-04-06T12:43:10Z",
    "updateDateIncludingText": "2026-04-06T12:43:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "IN"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1282ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1282\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Bilirakis (for himself and Mr. Baird ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo prohibit Federal funding for institutions of higher education that carry out diversity, equity, and inclusion initiatives, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Eliminate DEI in Colleges Act .\n#### 2. Prohibition on Federal funding for institutions of higher education that carry out diversity, equity, and inclusion initiatives\nPart B of title I of the Higher Education Act of 1965 ( 20 U.S.C. 1011 et seq. ) is amended by adding at the end the following:\n124. Prohibition on diversity, equity, and inclusion initiatives (a) Restriction on eligibility Notwithstanding any other provision of law, no institution of higher education shall be eligible to receive funds or any other form of financial assistance under any Federal program, including participation in any federally funded or guaranteed student loan program, unless the institution certifies to the Secretary that the institution\u2014 (1) does not and will not carry out any program, project, initiative, or other activity the primary purpose of which is to advocate, promote, or otherwise support diversity, equity, and inclusion; and (2) does not and will not maintain any office or other entity within the institution to advocate, promote, or otherwise support diversity, equity, and inclusion. (b) Information availability Each institution of higher education that provides the certification required by subsection (a) shall, upon request, make available to the Secretary any information needed by the Secretary to verify the truth and accuracy of the certification. (c) Regulations The Secretary shall publish regulations to implement and enforce the provisions of this section. (d) Appeals Upon determination by the Secretary to terminate financial assistance to any institution of higher education under this section, the institution may file an appeal with an administrative law judge before the expiration of the 30-day period beginning on the date such institution is notified of the decision to terminate financial assistance under this section. Such judge shall hold a hearing with respect to such termination of assistance before the expiration of the 45-day period beginning on the date that such appeal is filed. Such judge may extend such 45-day period upon a motion by the institution concerned. The decision of the judge with respect to such termination shall be considered to be a final agency action. (e) Definition In this section, the term diversity, equity, and inclusion means the concept according to which individuals are\u2014 (1) classified on basis of race, color, sex, national origin, gender identity, or sexual orientation; and (2) afforded differential or preferential treatment basis of such classification. .",
      "versionDate": "2025-02-13",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2026-04-06T12:42:55Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2026-04-06T12:42:41Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2026-04-06T12:43:05Z"
          },
          {
            "name": "School administration",
            "updateDate": "2026-04-06T12:42:59Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2026-04-06T12:43:10Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2026-04-06T12:42:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-17T15:49:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1282",
          "measure-number": "1282",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2025-07-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1282v00",
            "update-date": "2025-07-30"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Eliminate DEI in Colleges Act</strong></p><p>This bill prohibits an institution of higher education (IHE) from receiving federal funds or participating in federal student aid programs if the IHE carries out diversity, equity, and inclusion (DEI) initiatives.</p><p>Specifically, the bill requires an IHE to certify to the Department of Education (ED) that the\u00a0IHE (1) does not and will not carry out any program, project, initiative, or other activity that advocates, promotes, or otherwise supports DEI;\u00a0and (2) does not and will not maintain any office or other entity within the IHE that advocates, promotes, or otherwise supports DEI.</p><p>Each IHE that provides the certification must, upon request, make available to ED any information necessary to verify the accuracy of the certification.\u00a0</p><p>ED must publish regulations to implement and enforce the bill's provisions.\u00a0</p><p>The bill establishes a process through which an IHE may appeal ED's decision to terminate the IHE's financial assistance for failure to comply with the bill's provisions.</p>"
        },
        "title": "Eliminate DEI in Colleges Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1282.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Eliminate DEI in Colleges Act</strong></p><p>This bill prohibits an institution of higher education (IHE) from receiving federal funds or participating in federal student aid programs if the IHE carries out diversity, equity, and inclusion (DEI) initiatives.</p><p>Specifically, the bill requires an IHE to certify to the Department of Education (ED) that the\u00a0IHE (1) does not and will not carry out any program, project, initiative, or other activity that advocates, promotes, or otherwise supports DEI;\u00a0and (2) does not and will not maintain any office or other entity within the IHE that advocates, promotes, or otherwise supports DEI.</p><p>Each IHE that provides the certification must, upon request, make available to ED any information necessary to verify the accuracy of the certification.\u00a0</p><p>ED must publish regulations to implement and enforce the bill's provisions.\u00a0</p><p>The bill establishes a process through which an IHE may appeal ED's decision to terminate the IHE's financial assistance for failure to comply with the bill's provisions.</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119hr1282"
    },
    "title": "Eliminate DEI in Colleges Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Eliminate DEI in Colleges Act</strong></p><p>This bill prohibits an institution of higher education (IHE) from receiving federal funds or participating in federal student aid programs if the IHE carries out diversity, equity, and inclusion (DEI) initiatives.</p><p>Specifically, the bill requires an IHE to certify to the Department of Education (ED) that the\u00a0IHE (1) does not and will not carry out any program, project, initiative, or other activity that advocates, promotes, or otherwise supports DEI;\u00a0and (2) does not and will not maintain any office or other entity within the IHE that advocates, promotes, or otherwise supports DEI.</p><p>Each IHE that provides the certification must, upon request, make available to ED any information necessary to verify the accuracy of the certification.\u00a0</p><p>ED must publish regulations to implement and enforce the bill's provisions.\u00a0</p><p>The bill establishes a process through which an IHE may appeal ED's decision to terminate the IHE's financial assistance for failure to comply with the bill's provisions.</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119hr1282"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1282ih.xml"
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
      "title": "Eliminate DEI in Colleges Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Eliminate DEI in Colleges Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal funding for institutions of higher education that carry out diversity, equity, and inclusion initiatives, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T09:18:21Z"
    }
  ]
}
```
