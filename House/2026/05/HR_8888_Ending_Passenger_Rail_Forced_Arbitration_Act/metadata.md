# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8888?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8888
- Title: Ending Passenger Rail Forced Arbitration Act
- Congress: 119
- Bill type: HR
- Bill number: 8888
- Origin chamber: House
- Introduced date: 2026-05-19
- Update date: 2026-05-28T06:53:29Z
- Update date including text: 2026-05-28T06:53:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-19: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-05-19: Introduced in House

## Actions

- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-19",
    "latestAction": {
      "actionDate": "2026-05-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8888",
    "number": "8888",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "D000530",
        "district": "17",
        "firstName": "Christopher",
        "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
        "lastName": "Deluzio",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Ending Passenger Rail Forced Arbitration Act",
    "type": "HR",
    "updateDate": "2026-05-28T06:53:29Z",
    "updateDateIncludingText": "2026-05-28T06:53:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-19",
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
          "date": "2026-05-19T16:05:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8888ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8888\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2026 Mr. Deluzio (for himself and Mr. Boyle of Pennsylvania ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to prohibit Amtrak from including mandatory arbitration clauses in contracts of carriage, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ending Passenger Rail Forced Arbitration Act .\n#### 2. No validity or enforceability of arbitration agreements for consumer and civil rights disputes\n##### (a) In general\nChapter 243 of title 49, United States Code, is amended by adding at the end the following:\n24324. Prohibition on mandatory arbitration (a) Purposes The purposes of this section are\u2014 (1) to prohibit predispute arbitration agreements that force arbitration of consumer and civil rights disputes between Amtrak and customers of Amtrak; and (2) to prohibit agreements and practices that interfere with the right of customers to participate in a joint, class, or collective action related to consumer and civil rights disputes between Amtrak and customers of Amtrak. (b) Definitions In this section: (1) Amtrak The term Amtrak means the National Railroad Passenger Corporation. (2) Civil rights dispute The term civil rights dispute means a dispute\u2014 (A) arising from an alleged violation of\u2014 (i) the Constitution of the United States or the constitution of a State; or (ii) any Federal, State, or local law that prohibits discrimination on the basis of\u2014 (I) race, sex, age, gender identity, sexual orientation, disability, religion, or national origin; or (II) any legally protected status in education, employment, credit, housing, public accommodations and facilities, voting, veterans and servicemembers, health care, or a program funded or conducted by the Federal Government or a State government, including any law referred to or described in section 62(e) of the Internal Revenue Code of 1986, including parts of such law not explicitly referenced in such section that relate to protecting individuals on any such basis; and (B) in which at least 1 party alleging a violation described in subparagraph (A) consists of 1 or more customers (or their authorized representative), including 1 or more individuals seeking certification as a class under rule 23 of the Federal Rules of Civil Procedure or a comparable rule or provision of State law. (3) Consumer dispute The term consumer dispute means any dispute, including all claims related to personal injuries, between Amtrak and 1 or more customers who seek or acquire\u2014 (A) services and accommodations provided by Amtrak; or (B) carriage on Amtrak trains and equipment. (4) Customer The term customer means any individual, except for an employee of Amtrak and without regard to whether the individual is a minor or paid for the transportation, who seeks or acquires\u2014 (A) services and accommodations provided by Amtrak; or (B) carriage on Amtrak trains and equipment. (5) Predispute arbitration agreement The term predispute arbitration agreement means an agreement to arbitrate a dispute that has not yet arisen at the time of the making of the agreement. (6) Predispute joint-action waiver The term predispute joint-action waiver means an agreement, whether or not part of a predispute arbitration agreement, which would prohibit, or waive the right of, 1 of the parties to the agreement to participate in a joint, class, or collective action in a judicial, arbitral, administrative, or other forum, concerning a dispute that has not yet arisen at the time of the making of the agreement. (7) Rail passenger carrier The term rail passenger carrier means a rail carrier providing\u2014 (A) intercity rail passenger transportation (as such term is defined in section 24102); or (B) interstate or intrastate high-speed rail (as such term is defined in section 26105) transportation, excluding a tourist, historic, scenic, or excursion rail carrier. (c) In general (1) In general All predispute arbitration agreements and predispute joint-action waivers shall be invalid and unenforceable with respect to a consumer or civil rights dispute between Amtrak (in its capacity as a rail passenger carrier) and a customer of Amtrak. (2) Applicability (A) In general A determination of whether this section applies to a particular dispute shall be made in accordance with Federal law. (B) Authority of court The applicability of this section to an agreement to arbitrate and the validity and enforceability of an agreement to which this section applies shall be determined by a court, rather than by an arbitrator, regardless of whether\u2014 (i) the party resisting arbitration challenges the arbitration agreement specifically or in conjunction with other terms of the contract containing such agreement; and (ii) the agreement purports to delegate such determinations to an arbitrator. (C) Exclusion Nothing in this section may be construed to apply to a predispute arbitration agreement or joint-action waiver invoked in connection with any dispute subject to the Railway Labor Act ( 45 U.S.C. 151 et seq. ). .\n##### (b) Effective date\nThe amendment made by subsection (a)\u2014\n**(1)**\nshall take effect on the date of the enactment of this Act; and\n**(2)**\nshall apply with respect to any dispute or claim that arises or accrues on or after such date.\n##### (c) Clerical amendment\nThe analysis for chapter 243 of title 49, United States Code, is amended by adding at the end the following:\n24324. Prohibition on mandatory arbitration. .",
      "versionDate": "2026-05-19",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8888ih.xml"
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
      "title": "Ending Passenger Rail Forced Arbitration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-28T06:53:28Z"
    },
    {
      "title": "Ending Passenger Rail Forced Arbitration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-28T06:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to prohibit Amtrak from including mandatory arbitration clauses in contracts of carriage, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-28T06:48:28Z"
    }
  ]
}
```
