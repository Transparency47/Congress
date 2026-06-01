# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3010?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3010
- Title: No Handouts for Drug Advertisements Act
- Congress: 119
- Bill type: HR
- Bill number: 3010
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2025-12-05T21:46:43Z
- Update date including text: 2025-12-05T21:46:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3010",
    "number": "3010",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001210",
        "district": "3",
        "firstName": "Gregory",
        "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
        "lastName": "Murphy",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "No Handouts for Drug Advertisements Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:46:43Z",
    "updateDateIncludingText": "2025-12-05T21:46:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
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
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-24",
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
          "date": "2025-04-24T15:07:05Z",
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MN"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas [R-AK-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "AK"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MI"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3010ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3010\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Mr. Murphy (for himself, Ms. Craig , Mr. Begich , and Ms. Scholten ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to deny the deduction for advertising and promotional expenses for certain drugs.\n#### 1. Short title\nThis Act may be cited as the No Handouts for Drug Advertisements Act .\n#### 2. Disallowance of deduction for advertising and promotional expenses for certain drugs\n##### (a) In general\nPart IX of subchapter B of chapter 1 of subtitle A of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n280I. Disallowance of deduction for direct-to-consumer advertising of certain drugs (a) In general No deduction shall be allowed under this chapter for expenses relating to direct-to-consumer advertising of covered drugs for any taxable year. (b) Direct-to-Consumer advertising For purposes of this section\u2014 (1) In general The term direct-to-consumer advertising means any dissemination, by or on behalf of a covered entity, of an advertisement which\u2014 (A) is in regard to a covered drug, and (B) primarily targeted to the general public, including through\u2014 (i) broadcasting through media such as radio, television, and telephone communication systems, direct mail, and billboards, and (ii) dissemination on the Internet or through digital platforms (including social media, mobile media, web applications, digital applications, mobile applications, and electronic applications). (2) Exception Such term shall not include an advertisement made through publication in journals and other periodicals. (3) Other terms For purposes of this subsection\u2014 (A) Covered entity The term covered entity means\u2014 (i) a sponsor of a prescription drug product (as such term is defined in section 735(3) of the Federal Food, Drug, and Cosmetic Act), or (ii) a person that owns an outsourcing facility (as such term is defined in section 503B(d)(4) of such Act), either directly or indirectly through a subsidiary. (B) Covered drug The term covered drug means\u2014 (i) a prescription drug product (as such term is defined in section 735(3) of the Federal Food, Drug, and Cosmetic Act), or (ii) a drug compounded in accordance with section 503A or 503B of such Act. .\n##### (b) Conforming amendment\nThe table of sections for such part IX of the Internal Revenue Code of 1986 is amended by adding after the item relating to section 280H the following new item:\nSec. 280I. Disallowance of deduction for direct-to-consumer advertising of certain drugs. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred after the date of the enactment of this Act, in taxable years ending after such date.",
      "versionDate": "2025-04-24",
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
        "actionDate": "2025-05-15",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1785",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Handouts for Drug Advertisements Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-28T16:06:00Z"
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
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3010ih.xml"
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
      "title": "No Handouts for Drug Advertisements Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-08T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Handouts for Drug Advertisements Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-08T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to deny the deduction for advertising and promotional expenses for certain drugs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-08T05:18:33Z"
    }
  ]
}
```
