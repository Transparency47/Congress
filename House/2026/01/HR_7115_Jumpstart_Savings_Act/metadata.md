# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7115?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7115
- Title: Jumpstart Savings Act
- Congress: 119
- Bill type: HR
- Bill number: 7115
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-02-12T09:06:26Z
- Update date including text: 2026-02-12T09:06:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7115",
    "number": "7115",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001235",
        "district": "2",
        "firstName": "Riley",
        "fullName": "Rep. Moore, Riley M. [R-WV-2]",
        "lastName": "Moore",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Jumpstart Savings Act",
    "type": "HR",
    "updateDate": "2026-02-12T09:06:26Z",
    "updateDateIncludingText": "2026-02-12T09:06:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
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
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:04:25Z",
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
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "OH"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "IA"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "AL"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "AZ"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "UT"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2026-01-23",
      "state": "MN"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "WA"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "IN"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "TN"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "WI"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7115ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7115\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Moore of West Virginia (for himself, Mr. Rulli , Mrs. Hinson , Mr. Goldman of Texas , and Mr. Moore of Alabama ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish Jumpstart Programs for saving for apprenticeship and trade occupation training, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Jumpstart Savings Act .\n#### 2. Jumpstart Program\n##### (a) In general\nPart VIII of subchapter F of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 529A the following new section:\n529B. Jumpstart Program (a) In general A Jumpstart Program shall be exempt from taxation under this subtitle. Notwithstanding the preceding sentence, such program shall be subject to the taxes imposed by section 511 (relating to imposition of tax on unrelated business income of charitable organizations). (b) Jumpstart Program For purposes of this section\u2014 (1) In general The term Jumpstart Program means a program established and maintained by a State or agency or instrumentality thereof under which a person may make contributions to an account which is established for the purpose of meeting the qualified occupation, profession, or trade expenses of the designated beneficiary of the account. (2) Additional requirements A program shall not be treated as a Jumpstart Program unless such program meets rules similar to the rules of paragraphs (2), (3), (4), (5), and (6) of section 529(b). (c) Qualified occupation, profession, or trade expenses For purposes of this section, the term qualified occupation, profession, or trade expenses means\u2014 (1) expenses in connection with completing an apprenticeship program registered and certified with the Department of Labor, as provided in the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ), (2) tuition, fees, books, supplies, and equipment required for the enrollment or attendance of a designated beneficiary in an associate degree or certification program at a community and technical college, (3) fees for required certification or licensure for the beneficiary to practice a trade or occupation, (4) amounts paid or incurred for the purchase of tools and equipment acquired by the individual in the normal course of the practice of a trade or occupation, and (5) costs incurred by the beneficiary that are necessary to establish a business in a State in which the beneficiary will practice an occupation or profession when the costs are exclusively paid or incurred for the purpose of establishing and operating such business. (d) Tax treatment of designated beneficiaries and contributors For purposes of this section, rules similar to the rules of paragraphs (1), (2), (3), (4), and (5) of section 529(c) shall apply to Jumpstart Accounts in the same manner as applied to qualified tuition programs described in section 529(b)(1)(A)(ii). (e) Designated beneficiary The term designated beneficiary means\u2014 (1) the individual designated at the commencement of participation in the Jumpstart Program as the beneficiary of amounts paid (or to be paid) to the program, and (2) in the case of a change in beneficiaries under rules similar to the rules of section 529(c)(3)(C), the individual who is the new beneficiary. (f) Reports Each officer or employee having control of the Jumpstart Program or their designee shall make such reports regarding such program to the Secretary and to designated beneficiaries with respect to contributions, distributions, and such other matters as the Secretary may require. The reports required by this paragraph shall be filed at such time and in such manner and furnished to such individuals at such time and in such manner as may be required by the Secretary. .\n##### (b) Rollover from qualified tuition programs\nSection 529(c)(3)(C)(i) of such Code is amended by striking or at the end of subclause (II), by striking the period at the end of subclause (III) and inserting , or , and by inserting after subclause (III) the following new subclause:\n(IV) to a Jumpstart Program (as defined in section 529B(b)(1)) of the designated beneficiary or a member of the family of the designated beneficiary. .\n##### (c) Failure to provided reports\nSection 6693(a)(2) of such Code is amended by redesignating subparagraphs (F) and (G) as subparagraphs (G) and (E), respectively, and by inserting after subparagraph (E) the following new subparagraph:\n(F) section 529B(f) (relating to Jumpstart Program), .\n##### (d) Clerical amendment\nThe table of sections for part VIII of subchapter F of chapter 1 is amended by inserting after the item relating to section 529A the following new item:\nSec. 529B. Jumpstart Program. .\n##### (e) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2026-01-15",
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
        "name": "Taxation",
        "updateDate": "2026-02-04T22:59:09Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7115ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to establish Jumpstart Programs for saving for apprenticeship and trade occupation training, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:36Z"
    },
    {
      "title": "Jumpstart Savings Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T10:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Jumpstart Savings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T10:53:14Z"
    }
  ]
}
```
