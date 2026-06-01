# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/152?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/152
- Title: Student Empowerment Act
- Congress: 119
- Bill type: S
- Bill number: 152
- Origin chamber: Senate
- Introduced date: 2025-01-20
- Update date: 2025-12-05T21:31:30Z
- Update date including text: 2025-12-05T21:31:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-20: Introduced in Senate
- 2025-01-20 - IntroReferral: Introduced in Senate
- 2025-01-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-20: Introduced in Senate

## Actions

- 2025-01-20 - IntroReferral: Introduced in Senate
- 2025-01-20 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-20",
    "latestAction": {
      "actionDate": "2025-01-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/152",
    "number": "152",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Student Empowerment Act",
    "type": "S",
    "updateDate": "2025-12-05T21:31:30Z",
    "updateDateIncludingText": "2025-12-05T21:31:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-20",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-20",
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
          "date": "2025-01-20T21:48:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sponsorshipDate": "2025-01-20",
      "state": "OK"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-20",
      "state": "SC"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-20",
      "state": "MT"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-20",
      "state": "UT"
    },
    {
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-01-20",
      "state": "WI"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-01-20",
      "state": "SD"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-20",
      "state": "MO"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s152is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 152\nIN THE SENATE OF THE UNITED STATES\nJanuary 20, 2025 Mr. Cruz (for himself, Mr. Lankford , Mr. Scott of South Carolina , Mr. Sheehy , Mr. Curtis , Mr. Johnson , Mr. Rounds , Mr. Schmitt , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to permit kindergarten through grade 12 educational expenses to be paid from a 529 account.\n#### 1. Short title\nThis Act may be cited as the Student Empowerment Act .\n#### 2. 529 account funding for homeschool and additional elementary and secondary expenses\n##### (a) In general\nSection 529(c)(7) of the Internal Revenue Code of 1986 is amended to read as follows:\n(7) Treatment of elementary and secondary tuition Any reference in this section to the term qualified higher education expense shall include a reference to the following expenses in connection with enrollment or attendance at, or for students enrolled at or attending, an elementary or secondary public, private, or religious school: (A) Tuition. (B) Curriculum and curricular materials. (C) Books or other instructional materials. (D) Online educational materials. (E) Tuition for tutoring or educational classes outside of the home, including at a tutoring facility, but only if the tutor or instructor is not related to the student and\u2014 (i) is licensed as a teacher in any State, (ii) has taught at an eligible educational institution, or (iii) is a subject matter expert in the relevant subject. (F) Fees for a nationally standardized norm-referenced achievement test, an advanced placement examination, or any examinations related to college or university admission. (G) Fees for dual enrollment in an institution of higher education. (H) Educational therapies for students with disabilities provided by a licensed or accredited practitioner or provider, including occupational, behavioral, physical, and speech-language therapies. Such term shall include expenses for the purposes described in subparagraphs (A) through (H) in connection with a homeschool (whether treated as a homeschool or a private school for purposes of applicable State law). .\n##### (b) Effective date\nThe amendment made by this section shall apply to distributions made after the date of the enactment of this Act.",
      "versionDate": "2025-01-20",
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
        "actionDate": "2025-02-04",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "939",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Student Empowerment Act",
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
        "updateDate": "2025-02-26T16:16:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-20",
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
          "measure-id": "id119s152",
          "measure-number": "152",
          "measure-type": "s",
          "orig-publish-date": "2025-01-20",
          "originChamber": "SENATE",
          "update-date": "2025-04-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s152v00",
            "update-date": "2025-04-29"
          },
          "action-date": "2025-01-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Student Empowerment Act</strong></p><p>This bill expands the education-related expenses that may be paid for with tax-free distributions from a qualified tuition program (also known as a 529 plan) to include certain expenses related to elementary, secondary, and homeschool education.</p><p>Under current law, distributions from a 529 plan are excluded from gross income if they are used to pay for qualified higher education expenses, which includes up to $10,000 (per year and per beneficiary) for tuition at an elementary or secondary public, private, or religious school.</p><p>The bill expands the education-related expenses that may be paid for with tax-free distributions from a 529 plan to include tuition related to\u00a0homeschooling and the following expenses related to elementary, secondary, and homeschool education:</p><ul><li>curriculum and curricular materials,</li><li>books or other instructional materials,</li><li>online educational materials,</li><li>tutoring or educational classes outside the home,</li><li>testing fees,</li><li>fees for dual enrollment in an institution of higher education, and</li><li>educational therapies for students with disabilities.</li></ul>"
        },
        "title": "Student Empowerment Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s152.xml",
    "summary": {
      "actionDate": "2025-01-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Student Empowerment Act</strong></p><p>This bill expands the education-related expenses that may be paid for with tax-free distributions from a qualified tuition program (also known as a 529 plan) to include certain expenses related to elementary, secondary, and homeschool education.</p><p>Under current law, distributions from a 529 plan are excluded from gross income if they are used to pay for qualified higher education expenses, which includes up to $10,000 (per year and per beneficiary) for tuition at an elementary or secondary public, private, or religious school.</p><p>The bill expands the education-related expenses that may be paid for with tax-free distributions from a 529 plan to include tuition related to\u00a0homeschooling and the following expenses related to elementary, secondary, and homeschool education:</p><ul><li>curriculum and curricular materials,</li><li>books or other instructional materials,</li><li>online educational materials,</li><li>tutoring or educational classes outside the home,</li><li>testing fees,</li><li>fees for dual enrollment in an institution of higher education, and</li><li>educational therapies for students with disabilities.</li></ul>",
      "updateDate": "2025-04-29",
      "versionCode": "id119s152"
    },
    "title": "Student Empowerment Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Student Empowerment Act</strong></p><p>This bill expands the education-related expenses that may be paid for with tax-free distributions from a qualified tuition program (also known as a 529 plan) to include certain expenses related to elementary, secondary, and homeschool education.</p><p>Under current law, distributions from a 529 plan are excluded from gross income if they are used to pay for qualified higher education expenses, which includes up to $10,000 (per year and per beneficiary) for tuition at an elementary or secondary public, private, or religious school.</p><p>The bill expands the education-related expenses that may be paid for with tax-free distributions from a 529 plan to include tuition related to\u00a0homeschooling and the following expenses related to elementary, secondary, and homeschool education:</p><ul><li>curriculum and curricular materials,</li><li>books or other instructional materials,</li><li>online educational materials,</li><li>tutoring or educational classes outside the home,</li><li>testing fees,</li><li>fees for dual enrollment in an institution of higher education, and</li><li>educational therapies for students with disabilities.</li></ul>",
      "updateDate": "2025-04-29",
      "versionCode": "id119s152"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s152is.xml"
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
      "title": "Student Empowerment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Student Empowerment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to permit kindergarten through grade 12 educational expenses to be paid from a 529 account.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:27Z"
    }
  ]
}
```
