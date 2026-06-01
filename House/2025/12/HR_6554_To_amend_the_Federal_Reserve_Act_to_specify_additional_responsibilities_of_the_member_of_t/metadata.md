# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6554?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6554
- Title: Community Bank Representation Act
- Congress: 119
- Bill type: HR
- Bill number: 6554
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-03-10T21:43:01Z
- Update date including text: 2026-03-10T21:43:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 29 - 22.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 458.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-533.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-533.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 29 - 22.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 458.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-533.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-533.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6554",
    "number": "6554",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "D000594",
        "district": "15",
        "firstName": "Monica",
        "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
        "lastName": "De La Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Community Bank Representation Act",
    "type": "HR",
    "updateDate": "2026-03-10T21:43:01Z",
    "updateDateIncludingText": "2026-03-10T21:43:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-02-25",
      "calendarNumber": {
        "calendar": "U00458"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 458.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-533.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-533.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 29 - 22.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
        "item": [
          {
            "date": "2026-02-25T18:51:50Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-17T18:56:15Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-16T18:56:05Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T15:05:50Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "TX"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6554ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6554\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Ms. De La Cruz introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Federal Reserve Act to specify additional responsibilities of the member of the Board of Governors of the Federal Reserve System who was appointed as the member with experience working in or supervising community banks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Community Bank Representation Act .\n#### 2. Community bank member of the Board of Governors\n##### (a) Federal Reserve Act\nSection 10 of the Federal Reserve Act is amended\u2014\n**(1)**\nin the first undesignated paragraph ( 12 U.S.C. 241 ), by striking having less than $10,000,000,000 in total assets ;\n**(2)**\nin the second undesignated paragraph ( 12 U.S.C. 242 ), by inserting after regulation of such firms. the following: The Chairman shall select one member of the Board with demonstrated primary experience working in or supervising community banks to develop policy recommendations for the Board regarding supervision and regulation of banking organizations supervised by the Board having less than $17,000,000,000 in total assets, and to oversee the supervision and regulation of such banking organizations. ;\n**(3)**\nin paragraph (12) ( 12 U.S.C. 247b )\u2014\n**(A)**\nby striking The Vice Chairman for Supervision and inserting the following:\n(A) Vice Chairman for Supervision The Vice Chairman for Supervision ;\n**(B)**\nby striking and at and inserting at ; and\n**(C)**\nby adding at the end the following:\n(B) Community bank member The member of the Board with demonstrated primary experience working in or supervising community banks selected by the Chairman to develop policy recommendations for the Board regarding supervision and regulation of banking organizations supervised by the Board having less than $17,000,000,000 in total assets, and to oversee the supervision and regulation of such banking organizations, if different than the Vice Chairman for Supervision, shall appear before the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives at semi-annual hearings regarding the efforts, activities, objectives, and plans of the Board with respect to the conduct of supervision and regulation of banking organizations supervised by the Board having less than $17,000,000,000 in total assets. ; and\n**(4)**\nby adding at the end the following:\n(13) Member of the Board for community banks annual threshold adjustment (A) In general At the end of each year for which the nominal gross domestic product of the United States increases (a covered year ), the Board shall adjust each dollar figure described in the second undesignated paragraph of this section, paragraph (12)(B) of this section, and section 1004(a)(3) of the Federal Financial Institutions Examination Council Act of 1978 by a percentage equal to the percentage increase (if any) between\u2014 (i) the nominal gross domestic product of the United States for the year, during the preceding 5 years, with respect to which the nominal gross domestic product of the United States was the highest; and (ii) the nominal gross domestic product of the United States for the covered year. (B) Determination of GDP In this paragraph, the Board shall use nominal gross domestic product statistics determined by the Bureau of Economic Analysis. .\n##### (b) Federal Financial Institutions Examination Council Act of 1978\nSection 1004(a)(3) of the Federal Financial Institutions Examination Council Act of 1978 ( 12 U.S.C. 3303(a)(2) ) is amended by adding at the end the following: and such Governor shall consult with the Governor with demonstrated primary experience working in or supervising community banks selected by the Chairman of the Board to develop policy recommendations for the Board regarding supervision and regulation of banking organizations supervised by the Board having less than $17,000,000,000 in total assets, and to oversee the supervision and regulation of such banking organizations, .",
      "versionDate": "2025-12-10",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6554rh.xml",
      "text": "IB\nUnion Calendar No. 458\n119th CONGRESS\n2d Session\nH. R. 6554\n[Report No. 119\u2013533]\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Ms. De La Cruz introduced the following bill; which was referred to the Committee on Financial Services\nFebruary 25, 2026 Additional sponsors: Mr. Williams of Texas , Mr. Sessions , and Mr. Nunn of Iowa\nFebruary 25, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on December 10, 2025\nA BILL\nTo amend the Federal Reserve Act to specify additional responsibilities of the member of the Board of Governors of the Federal Reserve System who was appointed as the member with experience working in or supervising community banks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Community Bank Representation Act .\n#### 2. Community bank member of the Board of Governors\n##### (a) Federal Reserve Act\nSection 10 of the Federal Reserve Act is amended\u2014\n**(1)**\nin the first undesignated paragraph ( 12 U.S.C. 241 ), by striking having less than $10,000,000,000 in total assets ;\n**(2)**\nin the second undesignated paragraph ( 12 U.S.C. 242 ), by inserting after regulation of such firms. the following: The Chairman shall select one member of the Board with demonstrated primary experience working in or supervising community banks to, in consultation with the Vice Chairman for Supervision and any other member of the Board with demonstrated primary experience working in or supervising community banks, develop policy recommendations for the Board regarding supervision and regulation of banking organizations supervised by the Board having less than $17,000,000,000 in total assets, and to oversee the supervision and regulation of such banking organizations in consultation with the Vice Chairman for Supervision and any other member of the Board with demonstrated primary experience working in or supervising community banks. ;\n**(3)**\nin paragraph (12) ( 12 U.S.C. 247b )\u2014\n**(A)**\nby striking The Vice Chairman for Supervision and inserting the following:\n(A) Vice Chairman for Supervision The Vice Chairman for Supervision ;\n**(B)**\nby striking and at and inserting at ; and\n**(C)**\nby adding at the end the following:\n(B) Community bank member The member of the Board with demonstrated primary experience working in or supervising community banks selected by the Chairman to develop policy recommendations for the Board regarding supervision and regulation of banking organizations supervised by the Board having less than $17,000,000,000 in total assets, and to oversee the supervision and regulation of such banking organizations, if different than the Vice Chairman for Supervision, shall appear before the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives at semi-annual hearings regarding the efforts, activities, objectives, and plans of the Board with respect to the conduct of supervision and regulation of banking organizations supervised by the Board having less than $17,000,000,000 in total assets. ; and\n**(4)**\nby adding at the end the following:\n(13) Member of the Board for community banks annual threshold adjustment (A) In general At the end of each year for which the nominal gross domestic product of the United States increases (a covered year ), the Board shall adjust each dollar figure described in the second undesignated paragraph of this section, paragraph (12)(B) of this section, and section 1004(a)(3) of the Federal Financial Institutions Examination Council Act of 1978 by a percentage equal to the percentage increase (if any) between\u2014 (i) the nominal gross domestic product of the United States for the year, during the preceding 5 years, with respect to which the nominal gross domestic product of the United States was the highest; and (ii) the nominal gross domestic product of the United States for the covered year. (B) Determination of GDP In this paragraph, the Board shall use nominal gross domestic product statistics determined by the Bureau of Economic Analysis. .\n##### (b) Federal Financial Institutions Examination Council Act of 1978\nSection 1004(a)(3) of the Federal Financial Institutions Examination Council Act of 1978 ( 12 U.S.C. 3303(a)(3) ) is amended by adding at the end the following: and such Governor shall consult with the Governor with demonstrated primary experience working in or supervising community banks selected by the Chairman of the Board to develop policy recommendations for the Board regarding supervision and regulation of banking organizations supervised by the Board having less than $17,000,000,000 in total assets, and to oversee the supervision and regulation of such banking organizations, .",
      "versionDate": "2026-02-25",
      "versionType": "Reported in House"
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
        "actionDate": "2026-03-04",
        "text": "Ordered to be Reported by the Yeas and Nays: 26 - 16."
      },
      "number": "6955",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Main Street Capital Access Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2026-01-02T18:34:46Z"
          },
          {
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2026-01-02T18:40:27Z"
          },
          {
            "name": "Banking and financial institutions regulation",
            "updateDate": "2026-01-02T18:40:20Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-02T18:35:08Z"
          },
          {
            "name": "Economic performance and conditions",
            "updateDate": "2026-01-02T18:39:55Z"
          },
          {
            "name": "Federal Reserve System",
            "updateDate": "2026-01-02T18:21:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-15T18:46:31Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6554ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6554rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Community Bank Representation Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-26T07:53:29Z"
    },
    {
      "title": "Community Bank Representation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-13T09:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Community Bank Representation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-13T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Reserve Act to specify additional responsibilities of the member of the Board of Governors of the Federal Reserve System who was appointed as the member with experience working in or supervising community banks, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-13T09:03:23Z"
    }
  ]
}
```
