# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8736?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8736
- Title: Restoration of Employment Choice for Adults with Disabilities Act
- Congress: 119
- Bill type: HR
- Bill number: 8736
- Origin chamber: House
- Introduced date: 2026-05-12
- Update date: 2026-05-22T08:07:16Z
- Update date including text: 2026-05-22T08:07:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 18 - 15.
- Latest action: 2026-05-12: Introduced in House

## Actions

- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 18 - 15.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8736",
    "number": "8736",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "G000576",
        "district": "6",
        "firstName": "Glenn",
        "fullName": "Rep. Grothman, Glenn [R-WI-6]",
        "lastName": "Grothman",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Restoration of Employment Choice for Adults with Disabilities Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:16Z",
    "updateDateIncludingText": "2026-05-22T08:07:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 18 - 15.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
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
      "actionDate": "2026-05-12",
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
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-12",
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
            "date": "2026-05-21T20:06:21Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-12T16:04:00Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "MO"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "UT"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "WI"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8736ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8736\nIN THE HOUSE OF REPRESENTATIVES\nMay 12, 2026 Mr. Grothman (for himself, Mrs. Wagner , and Mr. Owens ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Rehabilitation Act of 1973 to ensure workplace choice and opportunity for young adults with disabilities.\n#### 1. Short title\nThis Act may be cited as the Restoration of Employment Choice for Adults with Disabilities Act .\n#### 2. Use of subminimum wage\nSection 511 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794g ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the matter preceding paragraph (1)\u2014\n**(i)**\nby striking No and inserting Any ;\n**(ii)**\nby striking 24 or younger and inserting 18 or older ; and\n**(iii)**\nby striking unless and inserting if ; and\n**(B)**\nby inserting at the end the following new paragraph:\n(3) The individual chooses to accept employment with such entity. ;\n**(2)**\nin subsection (b)(2), by striking 24 and inserting 17 ;\n**(3)**\nin subsection (c), by inserting at the end the following new paragraph:\n(4) Other exceptions The entity described in subsection (a) can satisfy the requirements of paragraph (1)(A) with respect to an individual, if\u2014 (A) such entity makes documented efforts, at the intervals described in paragraph (2), to contact on behalf of the individual, the designated State unit for the counseling, information, and referrals described in paragraph (1)(A); and (B) such designated State unit fails to provide such counseling, information, and referrals after such documented efforts. ; and\n**(4)**\nin subsection (d)(1), by inserting before the period at the end the following: and, if such individual is employed by an entity described in subsection (a) at the time such documentation is made pursuant to such process, to make available copies of such documentation to the entity .\n#### 3. Application\nThe amendments made by this Act shall apply with respect to the employment of an individual on or after the date of enactment of this Act.",
      "versionDate": "2026-05-12",
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
        "name": "Labor and Employment",
        "updateDate": "2026-05-21T19:55:10Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8736ih.xml"
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
      "title": "Restoration of Employment Choice for Adults with Disabilities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-13T09:08:25Z"
    },
    {
      "title": "Restoration of Employment Choice for Adults with Disabilities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T09:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Rehabilitation Act of 1973 to ensure workplace choice and opportunity for young adults with disabilities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-13T09:03:27Z"
    }
  ]
}
```
