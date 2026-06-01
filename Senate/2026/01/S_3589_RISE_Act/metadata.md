# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3589?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3589
- Title: RISE Act
- Congress: 119
- Bill type: S
- Bill number: 3589
- Origin chamber: Senate
- Introduced date: 2026-01-07
- Update date: 2026-02-10T12:03:18Z
- Update date including text: 2026-02-10T12:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-07: Introduced in Senate
- 2026-01-07 - IntroReferral: Introduced in Senate
- 2026-01-07 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-01-07: Introduced in Senate

## Actions

- 2026-01-07 - IntroReferral: Introduced in Senate
- 2026-01-07 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-07",
    "latestAction": {
      "actionDate": "2026-01-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3589",
    "number": "3589",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "RISE Act",
    "type": "S",
    "updateDate": "2026-02-10T12:03:18Z",
    "updateDateIncludingText": "2026-02-10T12:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-07",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-07",
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
          "date": "2026-01-07T20:37:52Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NH"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "LA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "MD"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "IN"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "MN"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "AZ"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "MO"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3589is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3589\nIN THE SENATE OF THE UNITED STATES\nJanuary 7, 2026 Mr. Banks (for himself, Ms. Hassan , Mr. Cassidy , Mr. Van Hollen , Mr. Young , and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Higher Education Act of 1965 to provide students with disabilities and their families with access to critical information needed to select the right college and succeed once enrolled.\n#### 1. Short title\nThis Act may be cited as the Respond, Innovate, Succeed, and Empower Act or the RISE Act .\n#### 2. Perfecting amendment to the definition of disability\nSection 103(6) of the Higher Education Act of 1965 ( 20 U.S.C. 1003(6) ) is amended by striking section 3(2) and inserting section 3 .\n#### 3. Supporting students with disabilities to succeed once enrolled in college\nSection 487(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(a) ) is amended by adding at the end the following:\n(30) (A) The institution will carry out the following: (i) Adopt policies that make any of the following documentation submitted by an individual sufficient to establish that such individual is an individual with a disability: (I) Documentation that the individual has had an individualized education program (referred to in this paragraph as an IEP ) in accordance with section 614(d) of the Individuals with Disabilities Education Act, if the IEP for the student was utilized in high school. (II) Documentation describing services or accommodations provided to the individual pursuant to section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ) (referred to in this paragraph as a Section 504 plan ), if the Section 504 plan for the student was utilized in high school. (III) A plan or record of service for the individual from a private high school, a local educational agency, a State educational agency, or an institution of higher education provided in accordance with the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ). (IV) A record or evaluation from a relevant licensed professional finding that the individual has a disability. (V) A plan or record of disability from another institution of higher education. (VI) Documentation of a disability due to service in the uniformed services, as defined in section 484C(a). (ii) Adopt policies that are transparent and explicit regarding information about the process by which the institution determines eligibility for accommodations. (iii) Disseminate such information to students, parents, and faculty in an accessible format, including during any student orientation and making such information readily available on a public website of the institution. (B) Nothing in this paragraph shall be construed to preclude an institution from establishing less burdensome criteria than that described in subparagraph (A) to establish an individual as an individual with a disability and therefore eligible for accommodations. .\n#### 4. Authorization of funds for the national center for information and technical support for postsecondary students with disabilities\nSection 777(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1140q(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking From amounts appropriated under section 778, and inserting From amounts appropriated under paragraph (5), ; and\n**(2)**\nby adding at the end the following:\n(5) Authorization of appropriations There is authorized to be appropriated to carry out this subsection a total of $10,000,000 for fiscal years 2027 through 2031. .\n#### 5. Inclusion of information on students with disabilities\nSection 487(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(a) ), as amended by section 3, is further amended by adding at the end the following:\n(31) (A) The institution will submit, for inclusion in the Integrated Postsecondary Education Data System (IPEDS) or any other Federal postsecondary institution data collection effort, key data related to undergraduate students enrolled in the institution who are formally registered as students with disabilities with the institution\u2019s office of disability services (which, for purposes of this paragraph, includes an equivalent office), including\u2014 (i) the total number of students registered with the institution's office of disability services; (ii) the number of students accessing or receiving accommodations, as voluntarily reported to the institution\u2019s office of disability services; (iii) the percentage of undergraduate students enrolled in the institution who are registered with the institution's office of disability services; and (iv) the total number of undergraduate certificates or degrees awarded to students registered with the institution's office of disability services. (B) Notwithstanding subparagraph (A), an institution shall not be required to submit information under this paragraph if the number of such students would reveal personally identifiable information about an individual student. .\n#### 6. Rule of construction\nNone of the amendments made by this Act shall be construed to affect the meaning of the terms reasonable accommodation or record of impairment under the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ) or the rights or remedies provided under such Act.",
      "versionDate": "2026-01-07",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-02-05T19:43:57Z"
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
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3589is.xml"
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
      "title": "RISE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RISE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T11:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Respond, Innovate, Succeed, and Empower Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T11:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Higher Education Act of 1965 to provide students with disabilities and their families with access to critical information needed to select the right college and succeed once enrolled.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:52Z"
    }
  ]
}
```
