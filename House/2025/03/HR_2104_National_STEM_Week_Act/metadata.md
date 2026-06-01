# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2104?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2104
- Title: National STEM Week Act
- Congress: 119
- Bill type: HR
- Bill number: 2104
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-02-25T00:41:17Z
- Update date including text: 2026-02-25T00:41:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2104",
    "number": "2104",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "C001126",
        "district": "15",
        "firstName": "Mike",
        "fullName": "Rep. Carey, Mike [R-OH-15]",
        "lastName": "Carey",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "National STEM Week Act",
    "type": "HR",
    "updateDate": "2026-02-25T00:41:17Z",
    "updateDateIncludingText": "2026-02-25T00:41:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:02:10Z",
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
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "OH"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2104ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2104\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Carey (for himself and Mrs. Beatty ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo establish a National STEM Week to promote American innovation and enhance STEM education pathways for all students, including those in rural, urban, and underserved communities.\n#### 1. Short title\nThis Act may be cited as the National STEM Week Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nScience, technology, engineering, and mathematics (STEM) fields are crucial to the economic competitiveness and innovative capacity of the United States.\n**(2)**\nThere exists a need to enhance access to quality STEM education across all demographics and regions to address disparities in STEM participation and to ensure a diverse and capable future workforce.\n**(3)**\nInformal and formal learning environments, including afterschool programs and at-home activities, play significant roles in stimulating interest and proficiency in STEM subjects.\n**(4)**\nCollaborations between educational institutions, industry partners, and communities can effectively inspire and prepare students for careers in STEM.\n#### 3. Designation of National STEM Week\nThe National Science and Technology Foundation Committee on Science, Technology, Engineering, and Mathematics (CoSTEM) education, in consultation with other relevant stakeholders, shall designate a week each calendar year as National STEM Week .\n#### 4. Purposes of National STEM Week\n##### (a) Purposes\nThe purposes of National STEM Week are, through the programs and activities described subsection (b), to\u2014\n**(1)**\nhighlight the importance of STEM education in educational institutions across the country;\n**(2)**\nshowcase diverse career pathways within STEM fields in both classroom settings and informal learning environments;\n**(3)**\nencourage family engagement with STEM activities at home to foster a conducive learning environment;\n**(4)**\nfacilitate partnerships between educational institutions and industry leaders to provide students with real-world applications and mentorship opportunities in STEM fields; and\n**(5)**\nsupport States and local communities in developing and promoting their own STEM Week activities and resources, tailored to their unique educational and industrial landscapes.\n##### (b) Programs and activities\nDuring National STEM Week, the National Science and Technology Foundation Committee on Science, Technology, Engineering, and Mathematics (CoSTEM) shall carry out the following:\n**(1) Educational activities**\nEncourage educational institutions to participate in National STEM Week.\n**(2) Community and family engagement**\nEncourage families of students attending the educational institutions participating in National STEM Week to participate in STEM activities.\n**(3) Industry involvement**\nEncourage STEM industries to\u2014\n**(A)**\nengage with students enrolled in educational institutions by providing mentorship programs, site visits, and guest lectures; and\n**(B)**\nsupport STEM education initiatives at such educational institutions through funding, resources, and expertise.\n#### 5. Reporting and evaluation\nNot later than one year after the date of enactment of this Act, and on an annual basis thereafter, the National Science and Technology Foundation Committee on Science, Technology, Engineering, and Mathematics (CoSTEM) shall submit to Congress a report detailing the activities conducted under National STEM Week, including\u2014\n**(1)**\na summary of nationwide participation and activities;\n**(2)**\nan analysis of the impact of these activities on improving STEM education and closing educational gaps; and\n**(3)**\nrecommendations for improving future STEM Weeks based on feedback from participants and stakeholders.\n#### 6. Definitions\nIn this Act:\n**(1) Educational institution**\nThe term educational institution means any elementary school, secondary school, and institution of higher education.\n**(2) Elementary school; secondary school**\nThe terms elementary school and secondary school have the meanings given the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(3) Industry leader**\nThe term industry leader means an individual in a leadership position within an industry partner who has the authority to make strategic decisions and allocate resources to support the purposes of National STEM Week.\n**(4) Industry partner**\nThe term industry partner means a for-profit or nonprofit entity seeking to support the purposes of National STEM Week.\n**(5) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 ).\n**(6) STEM**\nThe term STEM means science, technology, engineering, and mathematics.\n**(7) State**\nThe term State means each of the 50 States, the Commonwealth of Puerto Rico, the District of Columbia, Guam, American Samoa, the Commonwealth of the Northern Mariana Islands, and the United States Virgin Islands.",
      "versionDate": "2025-03-14",
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
        "actionDate": "2026-02-12",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 339."
      },
      "number": "1070",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National STEM Week Act",
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
            "name": "Community life and organization",
            "updateDate": "2025-11-21T15:32:57Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-11-21T15:32:57Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-11-21T15:32:57Z"
          },
          {
            "name": "Educational guidance",
            "updateDate": "2025-11-21T15:32:57Z"
          },
          {
            "name": "Science and engineering education",
            "updateDate": "2025-11-21T15:32:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-31T15:39:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119hr2104",
          "measure-number": "2104",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2025-09-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2104v00",
            "update-date": "2025-09-03"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>National STEM Week Act</strong></p><p>This bill\u00a0requires the National Science and Technology Council's\u00a0Committee on STEM to designate a week each calendar year as National STEM Week. (STEM refers to science, technology, engineering, and mathematics.)</p><p>During this established week, the committee must encourage educational institutions (i.e., elementary schools, secondary schools, and institutions of higher education) to participate in the week and also encourage families of students\u00a0attending these educational institutions to participate in STEM activities. Additionally, the committee must encourage STEM industries to (1) engage with students enrolled in educational institutions by providing mentorship programs, site visits, and guest lectures; and (2) support STEM education initiatives at these educational institutions through funding, resources, and expertise.</p><p>The committee must annually report to Congress on the activities conducted during the established week.</p>"
        },
        "title": "National STEM Week Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2104.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>National STEM Week Act</strong></p><p>This bill\u00a0requires the National Science and Technology Council's\u00a0Committee on STEM to designate a week each calendar year as National STEM Week. (STEM refers to science, technology, engineering, and mathematics.)</p><p>During this established week, the committee must encourage educational institutions (i.e., elementary schools, secondary schools, and institutions of higher education) to participate in the week and also encourage families of students\u00a0attending these educational institutions to participate in STEM activities. Additionally, the committee must encourage STEM industries to (1) engage with students enrolled in educational institutions by providing mentorship programs, site visits, and guest lectures; and (2) support STEM education initiatives at these educational institutions through funding, resources, and expertise.</p><p>The committee must annually report to Congress on the activities conducted during the established week.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hr2104"
    },
    "title": "National STEM Week Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>National STEM Week Act</strong></p><p>This bill\u00a0requires the National Science and Technology Council's\u00a0Committee on STEM to designate a week each calendar year as National STEM Week. (STEM refers to science, technology, engineering, and mathematics.)</p><p>During this established week, the committee must encourage educational institutions (i.e., elementary schools, secondary schools, and institutions of higher education) to participate in the week and also encourage families of students\u00a0attending these educational institutions to participate in STEM activities. Additionally, the committee must encourage STEM industries to (1) engage with students enrolled in educational institutions by providing mentorship programs, site visits, and guest lectures; and (2) support STEM education initiatives at these educational institutions through funding, resources, and expertise.</p><p>The committee must annually report to Congress on the activities conducted during the established week.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hr2104"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2104ih.xml"
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
      "title": "National STEM Week Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:07Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National STEM Week Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a National STEM Week to promote American innovation and enhance STEM education pathways for all students, including those in rural, urban, and underserved communities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:19:10Z"
    }
  ]
}
```
