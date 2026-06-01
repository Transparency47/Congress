# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3593?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3593
- Title: Title VIII Nursing Workforce Reauthorization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3593
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2026-05-21T08:08:32Z
- Update date including text: 2026-05-21T08:08:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-09-10 - Committee: Referred to the Subcommittee on Health.
- 2025-09-10 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-09-10 - Committee: Referred to the Subcommittee on Health.
- 2025-09-10 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3593",
    "number": "3593",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000295",
        "district": "14",
        "firstName": "David",
        "fullName": "Rep. Joyce, David P. [R-OH-14]",
        "lastName": "Joyce",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Title VIII Nursing Workforce Reauthorization Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:32Z",
    "updateDateIncludingText": "2026-05-21T08:08:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
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
          "date": "2025-05-23T14:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-09-10T17:50:32Z",
                "name": "Reported by"
              },
              {
                "date": "2025-09-10T17:43:31Z",
                "name": "Markup by"
              },
              {
                "date": "2025-09-10T17:43:22Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
        }
      },
      "systemCode": "hsif00",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "OR"
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
      "sponsorshipDate": "2025-05-23",
      "state": "VA"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "IL"
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
      "sponsorshipDate": "2025-06-05",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "NY"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "AL"
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
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "WI"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3593ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3593\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Mr. Joyce of Ohio (for himself, Ms. Bonamici , Mrs. Kiggans of Virginia , and Ms. Underwood ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to reauthorize certain nursing workforce development programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Title VIII Nursing Workforce Reauthorization Act of 2025 .\n#### 2. Advanced nursing education grants\nSection 811 of the Public Health Service Act ( 42 U.S.C. 296j ) is amended\u2014\n**(1)**\nin subsection (a)(2), by striking programs. and inserting the following: \u201cprograms, including individuals enrolled in\u2014\n(A) authorized nurse practitioner programs described in subsection (c); (B) authorized nurse-midwifery programs described in subsection (d); (C) authorized nurse anesthesia programs described in subsection (e); and (D) authorized clinical nurse specialist programs described in subsection (f). ;\n**(2)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1), by striking midwives and inserting nurse-midwives ; and\n**(B)**\nin paragraph (2), by striking American College of Nurse-Midwives ; and\n**(3)**\nin subsection (h)(1)(A), by striking fees and inserting fees, including costs for clinical education and preceptors, .\n#### 3. Strengthening capacity for nurse education and practice\n##### (a) In general\nPart D of title VIII of the Public Health Service Act ( 42 U.S.C. 296p et seq. ) is amended\u2014\n**(1)**\nin the part heading, by striking basic ; and\n**(2)**\nin section 831 ( 42 U.S.C. 296p )\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (1), by striking or after the semicolon;\n**(ii)**\nin paragraph (2), by striking methodologies. and inserting methodologies, audiovisual or other equipment, simulation and augmented reality resources, telehealth technologies, and virtual and physical laboratories; or ; and\n**(iii)**\nby adding at the end the following:\n(3) increasing the number of faculty and students at schools of nursing in order to address nursing workforce shortages. ; and\n**(B)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (2), by striking and survivors of domestic violence and inserting survivors of domestic violence, and survivors of sexual assault ;\n**(ii)**\nin paragraph (3), by striking or after the semicolon;\n**(iii)**\nin paragraph (4), by striking the period and inserting ; or ; and\n**(iv)**\nby adding at the end the following:\n(5) partnering with a health care facility, nurse-managed health clinic, community health center, or other facility that provides health care in order to provide education opportunities for the purpose of establishing or expanding clinical education. .\n##### (b) Conforming amendment\nSection 806(f)(2)(C) of the Public Health Service Act ( 42 U.S.C. 296e(f)(2)(C) ) is amended by striking basic .\n#### 4. Authorization of appropriations\nSection 871 of the Public Health Service Act ( 42 U.S.C. 298d ) is amended\u2014\n**(1)**\nin subsection (a), by striking $137,837,000 for each of fiscal years 2021 through 2025 and inserting $184,337,000 for each of fiscal years 2026 through 2030 ; and\n**(2)**\nin subsection (b), by striking $117,135,000 for each of the fiscal years 2021 through 2025 and inserting $121,135,000 for each of fiscal years 2026 through 2030 .",
      "versionDate": "2025-05-23",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1874",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Title VIII Nursing Workforce Reauthorization Act of 2025",
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
            "name": "Employment and training programs",
            "updateDate": "2025-09-16T14:11:41Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-09-16T14:11:32Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-09-16T14:11:05Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-09-16T14:11:36Z"
          },
          {
            "name": "Nursing",
            "updateDate": "2025-09-16T14:11:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-06-03T12:34:41Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3593ih.xml"
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
      "title": "Title VIII Nursing Workforce Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Title VIII Nursing Workforce Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to reauthorize certain nursing workforce development programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:26Z"
    }
  ]
}
```
