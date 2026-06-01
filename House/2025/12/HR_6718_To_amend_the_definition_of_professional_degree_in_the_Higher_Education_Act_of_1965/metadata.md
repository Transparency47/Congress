# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6718?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6718
- Title: Professional Student Degree Act
- Congress: 119
- Bill type: HR
- Bill number: 6718
- Origin chamber: House
- Introduced date: 2025-12-15
- Update date: 2026-05-28T15:54:10Z
- Update date including text: 2026-05-28T15:54:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-15: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-12-15: Introduced in House

## Actions

- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-15",
    "latestAction": {
      "actionDate": "2025-12-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6718",
    "number": "6718",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Professional Student Degree Act",
    "type": "HR",
    "updateDate": "2026-05-28T15:54:10Z",
    "updateDateIncludingText": "2026-05-28T15:54:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-15",
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
      "actionDate": "2025-12-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-15",
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
          "date": "2025-12-15T17:02:45Z",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "NE"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "PA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "VA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "PA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "PA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "MO"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "PA"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "SD"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NH"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "SC"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "VA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "NJ"
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
      "sponsorshipDate": "2026-04-30",
      "state": "NC"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "FL"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2026-05-22",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6718ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6718\nIN THE HOUSE OF REPRESENTATIVES\nDecember 15, 2025 Mr. Lawler (for himself, Mr. Bacon , Mr. Bresnahan , and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the definition of professional degree in the Higher Education Act of 1965.\n#### 1. Short title\nThis Act may be cited as the Professional Student Degree Act .\n#### 2. Professional degree defined\nSection 455(a)(4)(C) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(a)(4)(C) ) is amended\u2014\n**(1)**\nin clause (ii), by striking , as defined under section 668.2 of title 34, Code of Federal Regulations (as in effect on the date of enactment of this paragraph), ; and\n**(2)**\nby adding at the end the following:\n(iii) Professional degree In this paragraph, the term professional degree \u2014 (I) means a degree that signifies both completion of the academic requirements for beginning practice in a given profession (for which professional licensure is also commonly required), and a level of professional skill beyond that normally required for a bachelor's degree, as determined by the Secretary; and (II) includes each of the following degrees: (aa) Pharmacy (Pharm.D.). (bb) Dentistry (D.D.S. or D.M.D.). (cc) Veterinary Medicine (D.V.M.). (dd) Chiropractic (D.C. or D.C.M.). (ee) Law (L.L.B. or J.D.). (ff) Medicine (M.D.). (gg) Optometry (O.D.). (hh) Osteopathic Medicine/Osteopathy (D.O.). (ii) Podiatric Medicine/Podiatry (D.P.M., D.P., or Pod.D.). (jj) Theology/Theological Studies (M.Div. or M.H.L.). (kk) Clinical Psychology (Psy.D. or Ph.D.). (ll) Ministry (D.Min.). (mm) Social Work (M.S.W. or D.S.W.). (nn) Audiology (Au.D.). (oo) Physician Assistant/Associate (M.P.A.S., M.S.P.A.S., M.M.S., or M.S.). (pp) Occupational Therapy (M.O.T. of O.T.D.). (qq) Physical Therapy (D.P.T.). (rr) Nursing (M.S.N., D.N.P., or Ph.D.). (ss) Public Health (M.P.H.). (tt) Business Administration and Management, General (M.B.A. or D.B.A.). (uu) Accounting (M.Acc. or M.S.A.). (vv) Architecture (M.Arch.). (ww) Education (M.A., M.S., M.A.T., M.Ed.). (xx) Special Education (M.Ed. or M.S.Ed.). (yy) Any other degree that meets the requirements of subclause (I), as determined by the Secretary. .",
      "versionDate": "2025-12-15",
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
        "actionDate": "2026-05-04",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "8659",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Nursing is a Professional Degree Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-05-07",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "8691",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Nursing is a Professional Degree Act",
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
        "name": "Education",
        "updateDate": "2026-01-09T15:16:49Z"
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
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6718ih.xml"
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
      "title": "Professional Student Degree Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-07T06:38:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Professional Student Degree Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-07T06:38:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the definition of professional degree in the Higher Education Act of 1965.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-07T06:33:19Z"
    }
  ]
}
```
