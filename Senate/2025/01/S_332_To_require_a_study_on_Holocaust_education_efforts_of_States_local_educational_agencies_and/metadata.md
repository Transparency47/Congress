# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/332?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/332
- Title: Holocaust Education and Antisemitism Lessons Act
- Congress: 119
- Bill type: S
- Bill number: 332
- Origin chamber: Senate
- Introduced date: 2025-01-30
- Update date: 2026-04-29T11:03:31Z
- Update date including text: 2026-04-29T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-30: Introduced in Senate
- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- Latest action: 2025-01-30: Introduced in Senate

## Actions

- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/332",
    "number": "332",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacklyn",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Holocaust Education and Antisemitism Lessons Act",
    "type": "S",
    "updateDate": "2026-04-29T11:03:31Z",
    "updateDateIncludingText": "2026-04-29T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-30",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
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
          "date": "2025-01-30T19:23:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-12-09T18:12:39Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-12-09T18:12:39Z",
                "name": "Hearings By (subcommittee)"
              }
            ]
          },
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "OK"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CT"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "AZ"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s332is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 332\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Ms. Rosen (for herself and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require a study on Holocaust education efforts of States, local educational agencies, and public elementary and secondary schools, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Holocaust Education and Antisemitism Lessons Act .\n#### 2. Study and report on Holocaust education\n##### (a) Study\nBeginning not later than 180 days after the date of enactment of this Act, the Director of the United States Holocaust Memorial Museum (referred to in this Act as the Director ) shall conduct a study on Holocaust education efforts in States, local educational agencies, and public elementary schools and secondary schools. Such study shall include an examination of\u2014\n**(1)**\nall States;\n**(2)**\na nationally representative sample of local educational agencies; and\n**(3)**\na representative sample of public elementary and secondary schools served by the local educational agencies being studied.\n##### (b) Elements\nIn conducting the study under subsection (a), the Director shall\u2014\n**(1)**\ndetermine whether States and local educational agencies being studied require Holocaust education as part of the curriculum taught in public elementary schools and secondary schools;\n**(2)**\nidentify States and local educational agencies being studied that have optional Holocaust education as part of the curriculum taught in public elementary schools and secondary schools;\n**(3)**\nidentify each State\u2019s standards and the requirements of the local educational agencies being studied relating to Holocaust education and summarize the status of the implementation of such standards and requirements, including\u2014\n**(A)**\nthe existence of a centralized apparatus at the State or local level that collects and disseminates Holocaust education curricula and materials;\n**(B)**\nthe existence of Holocaust education professional development opportunities for pre-service and in-service teachers;\n**(C)**\nthe involvement of informal educational organizations in implementing Holocaust education, including museums and cultural centers;\n**(D)**\nan assessment of the challenges or gaps that may prevent educators from fulfilling Holocaust education requirements;\n**(E)**\nthe identification of training and resources needed to support educators teaching about the Holocaust; and\n**(F)**\nthe adoption of United States Holocaust Memorial Museum resources by\u2014\n**(i)**\nentities at the State or local level that disseminate Holocaust education curricula; or\n**(ii)**\nlocal Holocaust museums and centers;\n**(4)**\ndetermine\u2014\n**(A)**\nthe range of intended outcomes from a Holocaust education unit at the State and local educational agency level; and\n**(B)**\nthe methods teachers are using that result in successfully achieving intended learning outcomes, which may include\u2014\n**(i)**\nin-class discussion;\n**(ii)**\neducational activities conducted outside the classroom, including homework assignments and experiential learning involving State and local organizations, such as museums and cultural centers;\n**(iii)**\nproject based learning;\n**(iv)**\neducational materials and activities that are developmentally appropriate and taught through a trauma-informed lens; and\n**(v)**\nintegration of lessons from the Holocaust across the curriculum and throughout the school year;\n**(5)**\nidentify the types of instructional materials used to teach students about the Holocaust, including the use of primary source material;\n**(6)**\nidentify\u2014\n**(A)**\nin what disciplines the Holocaust is being taught;\n**(B)**\nthe amount of time allotted in the required curriculum to teach about the Holocaust; and\n**(C)**\nthe comprehensiveness of the Holocaust education curriculum taught in public elementary schools and secondary schools, as indicated by the extent to which the curriculum addresses all elements and aspects of the Holocaust and is based on reliable educational resources, such as resources provided by the United States Holocaust Memorial Museum; and\n**(7)**\nidentify the approaches used by public elementary schools and secondary schools to assess outcomes using traditional and nontraditional assessments, including assessments of\u2014\n**(A)**\nstudents\u2019 knowledge of the Holocaust; and\n**(B)**\nstudents\u2019 ability to identify and analyze antisemitism, bigotry, hate, and genocide in historical and contemporary contexts.\n##### (c) Report\n**(1) In general**\nFollowing the completion of the study under subsection (a), the Director shall prepare and submit to Congress a report on the results of the study.\n**(2) Deadline for submittal**\nThe report under paragraph (1) shall be submitted not later than the earlier of\u2014\n**(A)**\n180 days after the completion of the study under subsection (a); or\n**(B)**\n3 years after the date of enactment of this Act.\n##### (d) Definitions\nIn this Act:\n**(1) ESEA terms**\nThe terms elementary school , local educational agency , secondary school , and State have the meanings given those terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Holocaust**\nThe term Holocaust has the meaning given that term in section 3 of the Never Again Education Act ( Public Law 116\u2013141 ; 36 U.S.C. 2301 note).\n**(3) Holocaust education**\nThe term Holocaust education means educational activities that are specifically intended\u2014\n**(A)**\nto improve students\u2019 awareness and understanding of the Holocaust;\n**(B)**\nto educate students on the lessons of the Holocaust as a means to raise awareness about the importance of preventing genocide, hate, and bigotry against any group of people; and\n**(C)**\nto study the history of antisemitism, its deep historical roots, the use of conspiracy theories and propaganda that target the Jewish people, and the shape-shifting nature of antisemitism over time.\n**(4) Project based learning**\nThe term project based learning means a teaching method through which students learn by actively engaging in real-world and personally meaningful projects.",
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
        "actionDate": "2025-01-28",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Holocaust Education and Antisemitism Lessons Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-25T17:45:14Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-03-25T17:45:14Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-25T17:45:14Z"
          },
          {
            "name": "Historical and cultural resources",
            "updateDate": "2025-03-25T17:45:14Z"
          },
          {
            "name": "Museums, exhibitions, cultural centers",
            "updateDate": "2025-03-25T17:45:14Z"
          },
          {
            "name": "Religion",
            "updateDate": "2025-03-25T17:45:14Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2025-03-25T17:45:14Z"
          },
          {
            "name": "War crimes, genocide, crimes against humanity",
            "updateDate": "2025-03-25T17:45:14Z"
          },
          {
            "name": "World history",
            "updateDate": "2025-03-25T17:45:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-06T16:55:38Z"
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
          "measure-id": "id119s332",
          "measure-number": "332",
          "measure-type": "s",
          "orig-publish-date": "2025-01-30",
          "originChamber": "SENATE",
          "update-date": "2025-03-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s332v00",
            "update-date": "2025-03-21"
          },
          "action-date": "2025-01-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Holocaust Education and Antisemitism Lessons Act</b></p> <p>This bill directs the U.S. Holocaust Memorial Museum to study and report on Holocaust education efforts in states, local educational agencies (LEAs), and public elementary and secondary schools. Among other elements, the study must (1) determine whether states and LEAs require Holocaust education as part of the curriculum taught in public elementary and secondary schools, (2) identify the standards and requirements relating to Holocaust education, and (3) identify the types of instructional material used to teach students about the Holocaust.</p>"
        },
        "title": "Holocaust Education and Antisemitism Lessons Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s332.xml",
    "summary": {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Holocaust Education and Antisemitism Lessons Act</b></p> <p>This bill directs the U.S. Holocaust Memorial Museum to study and report on Holocaust education efforts in states, local educational agencies (LEAs), and public elementary and secondary schools. Among other elements, the study must (1) determine whether states and LEAs require Holocaust education as part of the curriculum taught in public elementary and secondary schools, (2) identify the standards and requirements relating to Holocaust education, and (3) identify the types of instructional material used to teach students about the Holocaust.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119s332"
    },
    "title": "Holocaust Education and Antisemitism Lessons Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Holocaust Education and Antisemitism Lessons Act</b></p> <p>This bill directs the U.S. Holocaust Memorial Museum to study and report on Holocaust education efforts in states, local educational agencies (LEAs), and public elementary and secondary schools. Among other elements, the study must (1) determine whether states and LEAs require Holocaust education as part of the curriculum taught in public elementary and secondary schools, (2) identify the standards and requirements relating to Holocaust education, and (3) identify the types of instructional material used to teach students about the Holocaust.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119s332"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s332is.xml"
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
      "title": "Holocaust Education and Antisemitism Lessons Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Holocaust Education and Antisemitism Lessons Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a study on Holocaust education efforts of States, local educational agencies, and public elementary and secondary schools, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:29Z"
    }
  ]
}
```
