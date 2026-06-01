# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4271?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4271
- Title: Support our Firefighters Act
- Congress: 119
- Bill type: S
- Bill number: 4271
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-05-14T11:03:27Z
- Update date including text: 2026-05-14T11:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4271",
    "number": "4271",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Support our Firefighters Act",
    "type": "S",
    "updateDate": "2026-05-14T11:03:27Z",
    "updateDateIncludingText": "2026-05-14T11:03:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T22:00:04Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "MT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4271is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4271\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. Padilla (for himself and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 5, United States Code, to provide rest and recuperation leave for employees engaged in wildland firefighting, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Support our Firefighters Act .\n#### 2. Rest and recuperation leave for employees engaged in wildland firefighting\n##### (a) In general\nSubchapter II of chapter 63 of title 5, United States Code, is amended by adding at the end the following:\n6329e. Rest and recuperation leave for employees engaged in wildland firefighting (a) Definitions In this section\u2014 (1) the term applicable Secretary means the Secretary of Agriculture or the Secretary of the Interior, as applicable to a covered employee; (2) the term covered employee means an employee of the Forest Service or the Department of the Interior who\u2014 (A) qualifies as a wildland firefighter based on the definitions of the terms firefighter and wildland firefighter in section 5332a(a) (applying the definition of employee in section 6301(2) in lieu of the definition of employee in section 5331(a)); or (B) is certified by the applicable Secretary to perform wildland fire incident-related duties during the period the employee is deployed to respond to a qualifying incident; and (3) the term qualifying incident has the meaning given the term in section 5545c(a). (b) Rest and recuperation leave (1) In general A covered employee may receive paid rest and recuperation leave following the completion of service in which the covered employee is deployed to respond to a qualifying incident, subject to the policies prescribed under this subsection. (2) Prescription of policies The Secretary of Agriculture and the Secretary of the Interior shall, in the sole and exclusive discretion of the Secretaries acting jointly, prescribe uniform policies described in paragraph (1) after consulting with the other applicable Secretary. (3) Content of policies The policies prescribed under paragraph (2) may include\u2014 (A) a maximum period of days in which a covered employee is deployed to respond to a qualifying incident, which shall\u2014 (i) begin on the date on which the covered employee departs from the official duty station of the covered employee and end on the date on which the covered employee returns to the official duty station of the covered employee; and (ii) be followed by a minimum number of days of rest and recuperation for the covered employee; (B) a requirement to use 3 days of rest and recuperation leave after a 14-day period during which the covered employee is deployed to respond to a qualifying incident, excluding travel to and from assignments; or (C) a requirement to use 4 days of rest and recuperation leave after a 21-day period during which the covered employee is deployed to respond to a qualifying incident, including travel to and from assignments. (c) Use of leave (1) In general Rest and recuperation leave granted under this section\u2014 (A) shall be used during scheduled hours within the tour of duty of the applicable covered employee established for leave-charging purposes; (B) shall be paid in the same manner as annual leave; (C) shall be used immediately after a qualifying incident; and (D) may not be set aside for later use. (2) No payment A covered employee may not receive any payment for unused rest and recuperation leave granted under this section. (d) Intermittent work schedule A covered employee with an intermittent work schedule\u2014 (1) shall be excused from duty during the same period of time that other covered employees in the same circumstances are entitled to rest and recuperation leave; and (2) shall receive a payment as if the covered employee were entitled to rest and recuperation leave under subsection (b). .\n##### (b) Technical and conforming amendment\nThe table of sections for subchapter II of chapter 63 of title 5, United States Code, is amended by inserting after the item relating to section 6329d the following:\n6329e. Rest and recuperation leave for employees engaged in wildland firefighting. .\n#### 3. Transfer authority\nNotwithstanding section 40803(c)(2) of the Infrastructure Investment and Jobs Act ( 16 U.S.C. 6592(c)(2) ), not more than $5,000,000 of the unobligated balances of amounts made available under the heading Wildland Fire Management under the heading Forest Service under the heading Department of Agriculture in title VI of division J of that Act ( Public Law 117\u201358 ; 135 Stat. 1410) pursuant to section 40803(c)(2)(B) of that Act ( 16 U.S.C. 6592(c)(2)(B) ) may, as necessary to continue uninterrupted the Federal wildland firefighter base salary increase described in section 40803(d)(4)(B) of that Act ( 16 U.S.C. 6592(d)(4)(B) ), including premium pay authorized under section 1701 of the Extending Government Funding and Delivering Emergency Assistance Act ( 5 U.S.C. 5547 note) (as amended by this Act), be transferred to and merged with the amounts made available under the heading Wildland Fire Management under the heading Department-wide programs under the heading Department of the Interior in title VI of division J of that Act ( Public Law 117\u201358 ; 135 Stat. 1393).\n#### 4. Waiver of overtime caps for wildland firefighters\nSection 1701 of the Extending Government Funding and Delivering Emergency Assistance Act ( 5 U.S.C. 5547 note) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nin the first sentence, by striking or 2022 or 2023 or 2024 and inserting or any calendar year thereafter ; and\n**(B)**\nin the second sentence\u2014\n**(i)**\nby striking Services and inserting services ; and\n**(ii)**\nby striking subsection and inserting subsection. ;\n**(2)**\nin subsection (b), by striking 2021 or 2022 or 2023 or 2024 and inserting the applicable calendar year ; and\n**(3)**\nin subsection (c), by striking 2021 or 2022 or 2023 or 2024 and inserting the applicable calendar year .",
      "versionDate": "2026-03-26",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-20T23:28:23Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4271is.xml"
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
      "title": "Support our Firefighters Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Support our Firefighters Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 5, United States Code, to provide rest and recuperation leave for employees engaged in wildland firefighting, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T03:48:26Z"
    }
  ]
}
```
