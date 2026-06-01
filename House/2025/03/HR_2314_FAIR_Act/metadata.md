# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2314?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2314
- Title: FAIR Act
- Congress: 119
- Bill type: HR
- Bill number: 2314
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2026-05-14T08:07:58Z
- Update date including text: 2026-05-14T08:07:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-25: Introduced in House

## Actions

- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2314",
    "number": "2314",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001086",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
        "lastName": "Harshbarger",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "FAIR Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:07:58Z",
    "updateDateIncludingText": "2026-05-14T08:07:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:02:10Z",
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
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "ME"
    },
    {
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "MO"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "WV"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NC"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "PA"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "PA"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "AL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "TN"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "NE"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "TN"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "VA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "NM"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "UT"
    },
    {
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "AR"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2314ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2314\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mrs. Harshbarger (for herself, Ms. Pingree , Mr. Graves , Mrs. Miller of West Virginia , and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVIII of the Social Security Act to require hospitals with approved medical residency training programs to submit to the Secretary of Health and Human Services certain information regarding osteopathic and allopathic candidates for such programs.\n#### 1. Short title\nThis Act may be cited as the Fair Access In Residency Act of 2025 or the FAIR Act of 2025 .\n#### 2. Encouraging more equitable treatment of osteopathic and allopathic candidates in residency application and review process\n##### (a) In general\nSection 1886(d)(5)(B) of the Social Security Act ( 42 U.S.C. 1395ww(d)(5)(B) ) is amended\u2014\n**(1)**\nin clause (i), by inserting at the end the following new sentence: For discharges occurring on or after October 1, 2026, the amount determined under the previous sentence for a hospital shall be reduced by 2 percent for each prior fiscal year (beginning with fiscal year 2025) for which the hospital has not submitted to the Secretary the information described in subclause (xiv). ; and\n**(2)**\nby adding at the end the following new clause:\n(xiv) For purposes of clause (i), the information described in this clause is, with respect to a hospital and a fiscal year, the following: (I) The number of applicants for residency in each of the hospital\u2019s approved medical residency training programs beginning in such fiscal year\u2014 (aa) from osteopathic medical schools; and (bb) from allopathic medical schools. (II) The number of such applicants accepted into each such program beginning in such fiscal year from each such type of medical school. (III) An affirmation that\u2014 (aa) the policy of the hospital is to consider for acceptance to each such program applicants from both osteopathic and allopathic medical schools; and (bb) in the case that the hospital requires applicants to submit an examination score as a prerequisite for acceptance in such a program, the hospital accepts scores from, at the election of the applicant, either the Comprehensive Osteopathic Medical Licensing Examination of the United States or the United States Medical Licensing Examination. .\n##### (b) Publication\nThe Secretary of Health and Human Services shall publish on a public website the information described in subclauses (I) and (II) of section 1886(d)(5)(B)(xiv) of the Social Security Act, as added by subsection (a), and the affirmation described in subclause (III) of such section, that is submitted by a hospital with respect to an approved medical residency training program (as defined in section 1886(d)(h)(A) of the Social Security Act (42 U.S.C. 1395ww(d)(h)(A)) for each fiscal year (beginning with fiscal year 2025).\n##### (c) Rule of construction\nNothing in this Act shall be construed as federalizing medical education, or as establishing a mandate for an approved medical residency training program (as defined in section 1886(d)(h)(A) of the Social Security Act (42 U.S.C. 1395ww(d)(h)(A)) to accept students (or to accept a certain number of students) from osteopathic or allopathic medical schools.",
      "versionDate": "2025-03-25",
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
        "actionDate": "2025-09-04",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2715",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FAIR Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-09T15:59:57Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2314ih.xml"
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
      "title": "FAIR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T09:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAIR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T09:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Access In Residency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T09:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to require hospitals with approved medical residency training programs to submit to the Secretary of Health and Human Services certain information regarding osteopathic and allopathic candidates for such programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T09:48:26Z"
    }
  ]
}
```
