# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2955?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2955
- Title: Forced Abortion Prevention and Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 2955
- Origin chamber: Senate
- Introduced date: 2025-09-30
- Update date: 2026-05-15T11:03:25Z
- Update date including text: 2026-05-15T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in Senate
- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-09-30: Introduced in Senate

## Actions

- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2955",
    "number": "2955",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
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
    "title": "Forced Abortion Prevention and Accountability Act",
    "type": "S",
    "updateDate": "2026-05-15T11:03:25Z",
    "updateDateIncludingText": "2026-05-15T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-30",
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
        "item": [
          {
            "date": "2025-09-30T22:57:08Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-30T22:57:08Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NC"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "LA"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "TX"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "MT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "ID"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "TN"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-01",
      "state": "FL"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "TX"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "OK"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "LA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "AL"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "MS"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "SC"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "SD"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2955is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2955\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Mr. Banks (for himself, Mr. Budd , Mr. Cassidy , Mr. Cornyn , Mr. Daines , Mr. Risch , and Mr. Hagerty ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to establish Federal penalties for the knowing and intentional administration of any abortion-inducing drug to a woman without her informed consent, if the abortion-inducing drug has been shipped or transported in interstate commerce, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Forced Abortion Prevention and Accountability Act .\n#### 2. Protecting victims of forced abortions\n##### (a) In general\nChapter 74 of title 18, United States Code, is amended by inserting after section 1531 the following:\n1532. Forced abortions prohibited (a) In general Except as provided in subsection (c), whoever, in or affecting interstate or foreign commerce, knowingly and intentionally administers to a pregnant woman an abortion-inducing drug without the informed consent of the woman shall be fined under this title, imprisoned not more than 25 years, or both. (b) Attempts and conspiracies Whoever attempts or conspires to commit an offense under subsection (a) shall be subject to the same penalties as those prescribed for the offense. (c) Dual penalty If the non-consensual administration of an abortion-inducing drug as described in subsection (a) results in serious bodily injury or death to the woman to whom the abortion-inducing drug was administered, the offender shall be fined under this title, imprisoned for not more than 25 years in addition to any term of imprisonment under subsection (a), or both. (d) Civil remedy (1) In general A woman who was administered an abortion-inducing drug in violation of subsection (a) may, in a civil action against any person who administered the abortion-inducing drug, attempted to administer the abortion-inducing drug, or conspired to commit an offense described in subsection (a) or (b), obtain appropriate relief in accordance with paragraph (2). (2) Appropriate relief Appropriate relief in a civil action under this subsection includes\u2014 (A) objectively verifiable money damages for all injuries, psychological and physical, occasioned by the violation; (B) statutory damages equal to 3 times the cost of all injuries occasioned by the violation; and (C) punitive damages. (3) Attorney\u2019s fees for plaintiff The court shall award a reasonable attorney\u2019s fee as part of the costs to a prevailing plaintiff in a civil action under this subsection. (4) Attorney\u2019s fees for defendant If a defendant in a civil action under this subsection prevails and the court finds that the plaintiff\u2019s suit was frivolous, the court shall award a reasonable attorney\u2019s fee in favor of the defendant against the plaintiff. (e) Definitions In this section: (1) Abortion The term abortion means the use or prescription of any instrument, medicine, drug, or any other substance or device\u2014 (A) to intentionally kill the unborn child of a woman known to be pregnant; or (B) to intentionally terminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014 (i) after viability, to produce a live birth and preserve the life and health of the child born alive; or (ii) to remove a dead unborn child. (2) Abortion-inducing drug The term abortion-inducing drug means any drug, medicine, or substance prescribed, dispensed, or administered with the intent to cause an abortion, including mifepristone or misoprostol. (3) Conspires to commit an offense The term conspires to commit an offense includes selling, sending by shipping or mailing, or giving an abortion-inducing drug without taking reasonable measures to ensure the individual requesting the drug is a pregnant woman wishing to obtain an abortion. (4) Informed consent The term informed consent means voluntary, knowing agreement by a woman to ingest an abortion-inducing drug, given after being fully informed of the nature, purpose, risks, and potential consequences of the use of the abortion-inducing drug. (5) Serious bodily injury The term serious bodily injury has the meaning given the term in section 1365. (6) Unborn child The term unborn child has the meaning given the term in section 1841. .\n##### (b) Clerical amendment\nThe table of sections for chapter 74 of title 18, United States Code, is amended by adding at the end the following:\n1532. Forced abortions prohibited. .\n##### (c) Chapter heading amendments\n**(1) Chapter heading in chapter**\nThe chapter heading for chapter 74 of title 18, United States Code, is amended by striking Partial-birth abortions and inserting Abortions .\n**(2) Table of chapters for part I**\nThe item relating to chapter 74 in the table of chapters at the beginning of part I of title 18, United States Code, is amended by striking Partial-birth abortions and inserting Abortions .",
      "versionDate": "2025-09-30",
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
        "actionDate": "2025-12-04",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6466",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Forced Abortion Prevention and Accountability Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-10T18:57:50Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2955is.xml"
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
      "title": "Forced Abortion Prevention and Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Forced Abortion Prevention and Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to establish Federal penalties for the knowing and intentional administration of any abortion-inducing drug to a woman without her informed consent, if the abortion-inducing drug has been shipped or transported in interstate commerce, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:18:19Z"
    }
  ]
}
```
