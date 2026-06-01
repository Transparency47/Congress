# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1095?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1095
- Title: Stop STALLING Act
- Congress: 119
- Bill type: S
- Bill number: 1095
- Origin chamber: Senate
- Introduced date: 2025-03-24
- Update date: 2025-09-03T19:44:20Z
- Update date including text: 2025-09-03T19:44:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-24: Introduced in Senate
- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-04-03 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-04-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 45.
- Latest action: 2025-03-24: Introduced in Senate

## Actions

- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-04-03 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-04-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 45.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1095",
    "number": "1095",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Stop STALLING Act",
    "type": "S",
    "updateDate": "2025-09-03T19:44:20Z",
    "updateDateIncludingText": "2025-09-03T19:44:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 45.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-24",
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
      "actionDate": "2025-03-24",
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
            "date": "2025-04-10T20:24:48Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-03T14:15:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-24T21:55:34Z",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "IA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "IL"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CT"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "TX"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "VT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1095is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1095\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2025 Ms. Klobuchar (for herself, Mr. Grassley , Mr. Durbin , Mr. Blumenthal , Mr. Cruz , Mr. Welch , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo enable the Federal Trade Commission to deter filing of sham citizen petitions to cover an attempt to interfere with approval of a competing generic drug or biosimilar, to foster competition, and facilitate the efficient review of petitions filed in good faith to raise legitimate public health concerns, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Significant and Time-wasting Abuse Limiting Legitimate Innovation of New Generics Act or the Stop STALLING Act .\n#### 2. Federal Trade Commission enforcement against sham petitions\n##### (a) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Covered application**\nThe term covered application means an application filed pursuant to subsection (b)(2) or (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ).\n**(3) Covered petition**\nThe term covered petition means a petition, or a supplement to a petition, filed under section 505(q) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(q) ).\n**(4) Person**\nThe term person \u2014\n**(A)**\nmeans an individual or entity; and\n**(B)**\nincludes\u2014\n**(i)**\na successor or an assign of an entity;\n**(ii)**\na joint venture, subsidiary, partnership, division, group, or affiliate controlled by an entity; and\n**(iii)**\na successor or an assign of a joint venture, subsidiary, partnership, division, group, or affiliate controlled by an entity.\n**(5) Series of covered petitions**\nThe term series of covered petitions means any group of more than 1 covered petition relating to the same covered application.\n**(6) Sham**\nThe term sham means\u2014\n**(A)**\na covered petition that\u2014\n**(i)**\nis objectively baseless; and\n**(ii)**\nattempts to use a governmental process, as opposed to the outcome of that process, to interfere with the business of a competitor; or\n**(B)**\na series of covered petitions that attempts to use a governmental process, as opposed to the outcome of that process, to interfere with the business of a competitor.\n##### (b) Violation\nA person submitting or causing the submission of a covered petition or a series of covered petitions that is a sham shall be liable for engaging in an unfair method of competition under section 5(a)(1) of the Federal Trade Commission Act ( 15 U.S.C. 45(a)(1) ).\n##### (c) Civil action\n**(1) In general**\nIf the Commission has reason to believe that the submission of a covered petition or a series of covered petitions constitutes a violation of section 5(a)(1) of the Federal Trade Commission Act ( 15 U.S.C. 45(a)(1) ), the Commission may commence a civil action to recover a civil penalty and seek other appropriate relief in a district court of the United States against any person that submitted or caused to be submitted such covered petition or such series of covered petitions.\n**(2) Presumption**\nIn a civil action under paragraph (1), a covered petition shall be presumed to be part of a series of covered petitions that is a sham under subsection (b) of this section if\u2014\n**(A)**\nthe Secretary of Health and Human Services\u2014\n**(i)**\nhas determined that the covered petition was submitted with the primary purpose of delaying the approval of a covered application; and\n**(ii)**\nhas referred such determination to the Commission in writing, including a reasoned basis for the determination; and\n**(B)**\nthe covered petition was part of a series of covered petitions.\n**(3) Exception**\nThe presumption in paragraph (2) shall not apply if the defendant establishes, by a preponderance of the evidence, that the series of covered petitions that includes the covered petition referred to the Commission by the Secretary of Health and Human Services is not a sham.\n**(4) Civil penalty**\nIn an action under paragraph (1), any person that has been found liable for a violation of section 5(a)(1) of the Federal Trade Commission Act ( 15 U.S.C. 45(a)(1) ) shall be subject to a civil penalty for each violation of not more than the greater of\u2014\n**(A)**\nany revenue earned from the sale by such person of any drug product, referenced in a covered application that was the subject of a covered petition or a series of covered petitions that is a sham, during the period during which the covered petition or series of covered petitions was under review by the Secretary of Health and Human Services; or\n**(B)**\n$50,000 for each calendar day that each covered petition that is a sham or that was part of a series of covered petitions that is a sham was under review by the Secretary of Health and Human Services.\n**(5) Review of referral**\nNo referral by the Secretary of Health and Human Services under paragraph (2)(A) shall be subject to judicial review, except as a third-party claim asserted by the defendant under section 706(2)(A) of title 5, United States Code, against the Secretary of Health and Human Services or the Department of Health and Human Services, as part of a civil action commenced under paragraph (1).\n**(6) Antitrust laws**\nNothing in this section shall modify, impair, limit, or supersede the applicability of the antitrust laws, as defined in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12 ), and of section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) to the extent that it applies to unfair methods of competition.\n**(7) Rule of construction**\nThe civil penalty provided in this subsection is in addition to, and not in lieu of, any other remedies provided by Federal law, including under section 16 of the Clayton Act ( 15 U.S.C. 26 ) or under section 13(b) of the Federal Trade Commission Act ( 15 U.S.C. 53(b) ).\n##### (d) Applicability\nThis section shall apply to any covered petition submitted on or after the date of enactment of this Act.\n##### (e) Rule of construction\nNothing in this Act shall be construed to limit any authority of the Commission under any other provision of law.\n#### 3. Severability\nIf any provision of this Act or the application of such provision to any person or circumstance is held to be unconstitutional, the remainder of this Act and the application of the provisions of such Act to any person or circumstance shall not be affected.",
      "versionDate": "2025-03-24",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1095rs.xml",
      "text": "II\nCalendar No. 45\n119th CONGRESS\n1st Session\nS. 1095\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2025 Ms. Klobuchar (for herself, Mr. Grassley , Mr. Durbin , Mr. Blumenthal , Mr. Cruz , Mr. Welch , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nApril 10, 2025 Reported by Mr. Grassley , without amendment\nA BILL\nTo enable the Federal Trade Commission to deter filing of sham citizen petitions to cover an attempt to interfere with approval of a competing generic drug or biosimilar, to foster competition, and facilitate the efficient review of petitions filed in good faith to raise legitimate public health concerns, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Significant and Time-wasting Abuse Limiting Legitimate Innovation of New Generics Act or the Stop STALLING Act .\n#### 2. Federal Trade Commission enforcement against sham petitions\n##### (a) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Covered application**\nThe term covered application means an application filed pursuant to subsection (b)(2) or (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ).\n**(3) Covered petition**\nThe term covered petition means a petition, or a supplement to a petition, filed under section 505(q) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(q) ).\n**(4) Person**\nThe term person \u2014\n**(A)**\nmeans an individual or entity; and\n**(B)**\nincludes\u2014\n**(i)**\na successor or an assign of an entity;\n**(ii)**\na joint venture, subsidiary, partnership, division, group, or affiliate controlled by an entity; and\n**(iii)**\na successor or an assign of a joint venture, subsidiary, partnership, division, group, or affiliate controlled by an entity.\n**(5) Series of covered petitions**\nThe term series of covered petitions means any group of more than 1 covered petition relating to the same covered application.\n**(6) Sham**\nThe term sham means\u2014\n**(A)**\na covered petition that\u2014\n**(i)**\nis objectively baseless; and\n**(ii)**\nattempts to use a governmental process, as opposed to the outcome of that process, to interfere with the business of a competitor; or\n**(B)**\na series of covered petitions that attempts to use a governmental process, as opposed to the outcome of that process, to interfere with the business of a competitor.\n##### (b) Violation\nA person submitting or causing the submission of a covered petition or a series of covered petitions that is a sham shall be liable for engaging in an unfair method of competition under section 5(a)(1) of the Federal Trade Commission Act ( 15 U.S.C. 45(a)(1) ).\n##### (c) Civil action\n**(1) In general**\nIf the Commission has reason to believe that the submission of a covered petition or a series of covered petitions constitutes a violation of section 5(a)(1) of the Federal Trade Commission Act ( 15 U.S.C. 45(a)(1) ), the Commission may commence a civil action to recover a civil penalty and seek other appropriate relief in a district court of the United States against any person that submitted or caused to be submitted such covered petition or such series of covered petitions.\n**(2) Presumption**\nIn a civil action under paragraph (1), a covered petition shall be presumed to be part of a series of covered petitions that is a sham under subsection (b) of this section if\u2014\n**(A)**\nthe Secretary of Health and Human Services\u2014\n**(i)**\nhas determined that the covered petition was submitted with the primary purpose of delaying the approval of a covered application; and\n**(ii)**\nhas referred such determination to the Commission in writing, including a reasoned basis for the determination; and\n**(B)**\nthe covered petition was part of a series of covered petitions.\n**(3) Exception**\nThe presumption in paragraph (2) shall not apply if the defendant establishes, by a preponderance of the evidence, that the series of covered petitions that includes the covered petition referred to the Commission by the Secretary of Health and Human Services is not a sham.\n**(4) Civil penalty**\nIn an action under paragraph (1), any person that has been found liable for a violation of section 5(a)(1) of the Federal Trade Commission Act ( 15 U.S.C. 45(a)(1) ) shall be subject to a civil penalty for each violation of not more than the greater of\u2014\n**(A)**\nany revenue earned from the sale by such person of any drug product, referenced in a covered application that was the subject of a covered petition or a series of covered petitions that is a sham, during the period during which the covered petition or series of covered petitions was under review by the Secretary of Health and Human Services; or\n**(B)**\n$50,000 for each calendar day that each covered petition that is a sham or that was part of a series of covered petitions that is a sham was under review by the Secretary of Health and Human Services.\n**(5) Review of referral**\nNo referral by the Secretary of Health and Human Services under paragraph (2)(A) shall be subject to judicial review, except as a third-party claim asserted by the defendant under section 706(2)(A) of title 5, United States Code, against the Secretary of Health and Human Services or the Department of Health and Human Services, as part of a civil action commenced under paragraph (1).\n**(6) Antitrust laws**\nNothing in this section shall modify, impair, limit, or supersede the applicability of the antitrust laws, as defined in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12 ), and of section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) to the extent that it applies to unfair methods of competition.\n**(7) Rule of construction**\nThe civil penalty provided in this subsection is in addition to, and not in lieu of, any other remedies provided by Federal law, including under section 16 of the Clayton Act ( 15 U.S.C. 26 ) or under section 13(b) of the Federal Trade Commission Act ( 15 U.S.C. 53(b) ).\n##### (d) Applicability\nThis section shall apply to any covered petition submitted on or after the date of enactment of this Act.\n##### (e) Rule of construction\nNothing in this Act shall be construed to limit any authority of the Commission under any other provision of law.\n#### 3. Severability\nIf any provision of this Act or the application of such provision to any person or circumstance is held to be unconstitutional, the remainder of this Act and the application of the provisions of such Act to any person or circumstance shall not be affected.",
      "versionDate": "2025-04-10",
      "versionType": "Reported in Senate"
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
            "name": "Administrative remedies",
            "updateDate": "2025-04-07T15:50:04Z"
          },
          {
            "name": "Business ethics",
            "updateDate": "2025-04-07T15:50:04Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-04-07T15:50:04Z"
          },
          {
            "name": "Competition and antitrust",
            "updateDate": "2025-04-07T15:50:04Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2025-04-07T15:50:04Z"
          },
          {
            "name": "Drug safety, medical device, and laboratory regulation",
            "updateDate": "2025-04-07T15:50:04Z"
          },
          {
            "name": "Food and Drug Administration (FDA)",
            "updateDate": "2025-04-07T15:50:04Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-04-07T15:50:04Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-04-07T15:50:04Z"
          },
          {
            "name": "Public participation and lobbying",
            "updateDate": "2025-04-07T15:50:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-04-03T17:08:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-24",
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
          "measure-id": "id119s1095",
          "measure-number": "1095",
          "measure-type": "s",
          "orig-publish-date": "2025-03-24",
          "originChamber": "SENATE",
          "update-date": "2025-09-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1095v00",
            "update-date": "2025-09-03"
          },
          "action-date": "2025-03-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stop Significant and Time-wasting Abuse Limiting Legitimate Innovation of New Generics Act or the</strong> <strong>Stop STALLING Act</strong></p><p>This bill makes it an unfair method of competition to submit an objectively baseless petition to the Food and Drug Administration (FDA) in an attempt to interfere with a competitor's application for market approval of a drug.</p><p>The bill authorizes the Federal Trade Commission to sue an individual or entity that submits such a petition to the FDA. A party found liable in such a lawsuit is subject to civil penalties, such as a fine of up to $50,000 for each day that the FDA spent reviewing the baseless petition.</p>"
        },
        "title": "Stop STALLING Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1095.xml",
    "summary": {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Significant and Time-wasting Abuse Limiting Legitimate Innovation of New Generics Act or the</strong> <strong>Stop STALLING Act</strong></p><p>This bill makes it an unfair method of competition to submit an objectively baseless petition to the Food and Drug Administration (FDA) in an attempt to interfere with a competitor's application for market approval of a drug.</p><p>The bill authorizes the Federal Trade Commission to sue an individual or entity that submits such a petition to the FDA. A party found liable in such a lawsuit is subject to civil penalties, such as a fine of up to $50,000 for each day that the FDA spent reviewing the baseless petition.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119s1095"
    },
    "title": "Stop STALLING Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Significant and Time-wasting Abuse Limiting Legitimate Innovation of New Generics Act or the</strong> <strong>Stop STALLING Act</strong></p><p>This bill makes it an unfair method of competition to submit an objectively baseless petition to the Food and Drug Administration (FDA) in an attempt to interfere with a competitor's application for market approval of a drug.</p><p>The bill authorizes the Federal Trade Commission to sue an individual or entity that submits such a petition to the FDA. A party found liable in such a lawsuit is subject to civil penalties, such as a fine of up to $50,000 for each day that the FDA spent reviewing the baseless petition.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119s1095"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1095is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1095rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Stop STALLING Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-04-15T04:23:15Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Stop Significant and Time-wasting Abuse Limiting Legitimate Innovation of New Generics Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-04-15T04:23:15Z"
    },
    {
      "title": "Stop STALLING Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop STALLING Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Significant and Time-wasting Abuse Limiting Legitimate Innovation of New Generics Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to enable the Federal Trade Commission to deter filing of sham citizen petitions to cover an attempt to interfere with approval of a competing generic drug or biosimilar, to foster competition, and facilitate the efficient review of petitions filed in good faith to raise legitimate public health concerns, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:47Z"
    }
  ]
}
```
