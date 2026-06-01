# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8691?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8691
- Title: Nursing is a Professional Degree Act
- Congress: 119
- Bill type: HR
- Bill number: 8691
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-28T15:54:10Z
- Update date including text: 2026-05-28T15:54:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8691",
    "number": "8691",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Nursing is a Professional Degree Act",
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
      "actionDate": "2026-05-07",
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
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:03:10Z",
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
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "OH"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "MI"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
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
      "sponsorshipDate": "2026-05-07",
      "state": "NE"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "WA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "FL"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "FL"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8691ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8691\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mrs. Kiggans of Virginia (for herself, Mr. Joyce of Ohio , Mr. Bergman , Mr. Fitzpatrick , and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the definition of a professional student in the Higher Education Act of 1965.\n#### 1. Short title\nThis Act may be cited as the Nursing is a Professional Degree Act .\n#### 2. Professional student and professional degree defined\nSection 455(a)(4)(C) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(a)(4)(C) ) is amended\u2014\n**(1)**\nin clause (ii), by striking , as defined under section 668.2 of title 34, Code of Federal Regulations (as in effect on the date of enactment of this paragraph), ; and\n**(2)**\nby adding at the end the following:\n(iii) Professional degree In this paragraph, the term professional degree \u2014 (I) means a degree that signifies both completion of the academic requirements for beginning practice in a given profession (for which professional licensure is also commonly required) and a level of professional skill beyond that normally required for a bachelor\u2019s degree; and (II) includes each of the following degrees: (aa) Pharmacy (Pharm.D.). (bb) Dentistry (D.D.S. or D.M.D.). (cc) Veterinary Medicine (D.V.M.). (dd) Chiropractic (D.C. or D.C.M.). (ee) Law (L.L.B. or J.D.). (ff) Medicine (M.D.). (gg) Optometry (O.D.). (hh) Osteopathic Medicine/Osteopathy (D.O.). (ii) Podiatric Medicine/Podiatry (D.P.M., D.P., or Pod.D.). (jj) Theology/Theological Studies (M.Div. or M.H.L.). (kk) Clinical Psychology (Psy.D. or Ph.D.). (ll) Nursing (MSN, DNP, DNAP, or Ph.D). (mm) Any other degree that meets the requirements of subclause (I), as determined by the Secretary. .",
      "versionDate": "2026-05-07",
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
          "type": "Identical bill"
        }
      },
      "title": "Nursing is a Professional Degree Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-15",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "6718",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Professional Student Degree Act",
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
        "name": "Health",
        "updateDate": "2026-05-21T19:29:26Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8691ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Nursing is a Professional Degree Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T05:53:25Z"
    },
    {
      "title": "Nursing is a Professional Degree Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T05:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the definition of a professional student in the Higher Education Act of 1965.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T05:48:33Z"
    }
  ]
}
```
