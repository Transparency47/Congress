# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/939?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/939
- Title: Student Empowerment Act
- Congress: 119
- Bill type: HR
- Bill number: 939
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-12-05T21:31:35Z
- Update date including text: 2025-12-05T21:31:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/939",
    "number": "939",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001082",
        "district": "1",
        "firstName": "Kevin",
        "fullName": "Rep. Hern, Kevin [R-OK-1]",
        "lastName": "Hern",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Student Empowerment Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:31:35Z",
    "updateDateIncludingText": "2025-12-05T21:31:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:10:10Z",
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
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "PA"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NE"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "IA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "PA"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr939ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 939\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Hern of Oklahoma (for himself, Mr. Kelly of Pennsylvania , Mr. Smith of Nebraska , and Mrs. Hinson ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to permit kindergarten through grade 12 educational expenses to be paid from a 529 account.\n#### 1. Short title\nThis Act may be cited as the Student Empowerment Act .\n#### 2. 529 account funding for homeschool and additional elementary and secondary expenses\n##### (a) In general\nSection 529(c)(7) of the Internal Revenue Code of 1986 is amended to read as follows:\n(7) Treatment of elementary and secondary tuition Any reference in this section to the term qualified higher education expense shall include a reference to the following expenses in connection with enrollment or attendance at, or for students enrolled at or attending, an elementary or secondary public, private, or religious school: (A) Tuition. (B) Curriculum and curricular materials. (C) Books or other instructional materials. (D) Online educational materials. (E) Tuition for tutoring or educational classes outside of the home, including at a tutoring facility, but only if the tutor or instructor is not related to the student and\u2014 (i) is licensed as a teacher in any State, (ii) has taught at an eligible educational institution, or (iii) is a subject matter expert in the relevant subject. (F) Fees for a nationally standardized norm-referenced achievement test, an advanced placement examination, or any examinations related to college or university admission. (G) Fees for dual enrollment in an institution of higher education. (H) Educational therapies for students with disabilities provided by a licensed or accredited practitioner or provider, including occupational, behavioral, physical, and speech-language therapies. Such term shall include expenses for the purposes described in subparagraphs (A) through (H) in connection with a homeschool (whether treated as a homeschool or a private school for purposes of applicable State law). .\n##### (b) Effective date\nThe amendment made by this section shall apply to distributions made after the date of the enactment of this Act.",
      "versionDate": "2025-02-04",
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
        "actionDate": "2025-01-20",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "152",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Student Empowerment Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-28",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "750",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ACE Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-03",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "137",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "TCJA Permanency Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-29",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "311",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ACE Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-04",
        "text": "Became Public Law No: 119-21."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "An act to provide for reconciliation pursuant to title II of H. Con. Res. 14.",
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
        "name": "Taxation",
        "updateDate": "2025-04-16T15:26:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hr939",
          "measure-number": "939",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-04-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr939v00",
            "update-date": "2025-04-29"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Student Empowerment Act</strong></p><p>This bill expands the education-related expenses that may be paid for with tax-free distributions from a qualified tuition program (also known as a 529 plan) to include certain expenses related to elementary, secondary, and homeschool education.</p><p>Under current law, distributions from a 529 plan are excluded from gross income if they are used to pay for qualified higher education expenses, which includes up to $10,000 (per year and per beneficiary) for tuition at an elementary or secondary public, private, or religious school.</p><p>The bill expands the education-related expenses that may be paid for with tax-free distributions from a 529 plan to include tuition related to\u00a0homeschooling and the following expenses related to elementary, secondary, and homeschool education:</p><ul><li>curriculum and curricular materials,</li><li>books or other instructional materials,</li><li>online educational materials,</li><li>tutoring or educational classes outside the home,</li><li>testing fees,</li><li>fees for dual enrollment in an institution of higher education, and</li><li>educational therapies for students with disabilities.</li></ul>"
        },
        "title": "Student Empowerment Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr939.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Student Empowerment Act</strong></p><p>This bill expands the education-related expenses that may be paid for with tax-free distributions from a qualified tuition program (also known as a 529 plan) to include certain expenses related to elementary, secondary, and homeschool education.</p><p>Under current law, distributions from a 529 plan are excluded from gross income if they are used to pay for qualified higher education expenses, which includes up to $10,000 (per year and per beneficiary) for tuition at an elementary or secondary public, private, or religious school.</p><p>The bill expands the education-related expenses that may be paid for with tax-free distributions from a 529 plan to include tuition related to\u00a0homeschooling and the following expenses related to elementary, secondary, and homeschool education:</p><ul><li>curriculum and curricular materials,</li><li>books or other instructional materials,</li><li>online educational materials,</li><li>tutoring or educational classes outside the home,</li><li>testing fees,</li><li>fees for dual enrollment in an institution of higher education, and</li><li>educational therapies for students with disabilities.</li></ul>",
      "updateDate": "2025-04-29",
      "versionCode": "id119hr939"
    },
    "title": "Student Empowerment Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Student Empowerment Act</strong></p><p>This bill expands the education-related expenses that may be paid for with tax-free distributions from a qualified tuition program (also known as a 529 plan) to include certain expenses related to elementary, secondary, and homeschool education.</p><p>Under current law, distributions from a 529 plan are excluded from gross income if they are used to pay for qualified higher education expenses, which includes up to $10,000 (per year and per beneficiary) for tuition at an elementary or secondary public, private, or religious school.</p><p>The bill expands the education-related expenses that may be paid for with tax-free distributions from a 529 plan to include tuition related to\u00a0homeschooling and the following expenses related to elementary, secondary, and homeschool education:</p><ul><li>curriculum and curricular materials,</li><li>books or other instructional materials,</li><li>online educational materials,</li><li>tutoring or educational classes outside the home,</li><li>testing fees,</li><li>fees for dual enrollment in an institution of higher education, and</li><li>educational therapies for students with disabilities.</li></ul>",
      "updateDate": "2025-04-29",
      "versionCode": "id119hr939"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr939ih.xml"
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
      "title": "Student Empowerment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Student Empowerment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to permit kindergarten through grade 12 educational expenses to be paid from a 529 account.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:45Z"
    }
  ]
}
```
