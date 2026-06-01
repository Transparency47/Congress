# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1000?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1000
- Title: A bill to establish an Ambassador-at-Large for Arctic Affairs.
- Congress: 119
- Bill type: S
- Bill number: 1000
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2025-12-17T17:24:24Z
- Update date including text: 2025-12-17T17:24:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 231.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 231.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1000",
    "number": "1000",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "A bill to establish an Ambassador-at-Large for Arctic Affairs.",
    "type": "S",
    "updateDate": "2025-12-17T17:24:24Z",
    "updateDateIncludingText": "2025-12-17T17:24:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 231.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-22",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-12",
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
            "date": "2025-10-30T15:04:58Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-22T14:03:33Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-12T20:26:42Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-12",
      "state": "ME"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "AK"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "DE"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "SC"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "VT"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "ME"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MI"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MN"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NH"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-10-16",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1000is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1000\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Ms. Murkowski (for herself, Mr. King , Mr. Sullivan , Mr. Coons , Mr. Graham , Mr. Welch , Ms. Collins , Ms. Slotkin , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo establish an Ambassador-at-Large for Arctic Affairs.\n#### 1. Ambassador-at-Large for Arctic Affairs\nTitle I of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a et seq. ) is amended by adding at the end the following new section:\n65. United States Ambassador-at-Large for Arctic Affairs (a) Establishment There is authorized within the Department of State an Ambassador-at-Large for Arctic Affairs, appointed under subsection (b). (b) Appointment The Ambassador shall be appointed by the President, by, and with the advice and consent of the Senate. (c) Duties The Ambassador is authorized to represent the United States in matters and cases relevant to Arctic affairs and shall be responsible to the Secretary of State for all matters, programs, and related activities pertaining to the Arctic region in the conduct of foreign policy by the Department, including, as appropriate, leading the coordination of programs carried out by United States Government agencies abroad, and such other related duties as the Secretary may from time to time designate. (d) Areas of responsibility The Ambassador-at-Large for Arctic Affairs is authorized to maintain continuous observation and coordination of all matters indicated by the Secretary of State, including those pertaining to energy, environment, trade, and infrastructure development and maintenance, and, in consultation with the heads of other relevant departments and agencies, those pertaining to law enforcement and political-military affairs in the conduct of foreign policy in the Arctic, including programs carried out by other United States Government agencies when such programs pertain to the following matters, to the extent directed by the Secretary of State: (1) National security. (2) Strengthening cooperation among Arctic countries. (3) The promotion of responsible natural resource management and economic development. (4) Protecting the Arctic environment and conserving its biological resources. (5) Arctic indigenous peoples, including by involving them in decisions that affect them. (6) Scientific monitoring and research. (e) Additional duties In addition to the duties and responsibilities specified in subsections (c) and (d), the Ambassador-at-Large for Arctic Affairs shall also carry out such other relevant duties as the Secretary may assign. (f) Definitions In this section: (1) Arctic region The term Arctic region means\u2014 (A) the geographic region north of the 66.56083 parallel latitude north of the equator; (B) all the United States territory north and west of the boundary formed by the Porcupine, Yukon, and Kuskokwim Rivers; (C) all contiguous seas, including the Arctic Ocean and the Beaufort, Bering, and Chukchi Seas; and (D) the Aleutian Chain. (2) Arctic countries The term Arctic countries means the permanent members of the Arctic Council, namely the United States, Canada, Denmark, Iceland, Norway, Sweden, Finland, and Russia. .",
      "versionDate": "2025-03-12",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1000rs.xml",
      "text": "II\nCalendar No. 231\n119th CONGRESS\n1st Session\nS. 1000\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Ms. Murkowski (for herself, Mr. King , Mr. Sullivan , Mr. Coons , Mr. Graham , Mr. Welch , Ms. Collins , Ms. Slotkin , Ms. Klobuchar , Mrs. Shaheen , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nOctober 30, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo establish an Ambassador-at-Large for Arctic Affairs.\n#### 1. Ambassador-at-Large for Arctic Affairs\nTitle I of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a et seq. ) is amended by adding at the end the following new section:\n65. United States Ambassador-at-Large for Arctic Affairs (a) Establishment There is authorized within the Department of State an Ambassador-at-Large for Arctic Affairs, appointed under subsection (b). (b) Appointment The Ambassador shall be appointed by the President, by, and with the advice and consent of the Senate. (c) Duties The Ambassador is authorized to represent the United States in matters and cases relevant to Arctic affairs and shall be responsible to the Secretary of State for all matters, programs, and related activities pertaining to the Arctic region in the conduct of foreign policy by the Department, including, as appropriate, leading the coordination of programs carried out by United States Government agencies abroad, and such other related duties as the Secretary may from time to time designate. (d) Areas of responsibility The Ambassador-at-Large for Arctic Affairs is authorized to maintain continuous observation and coordination of all matters indicated by the Secretary of State, including those pertaining to energy, environment, trade, and infrastructure development and maintenance, and, in consultation with the heads of other relevant departments and agencies, those pertaining to law enforcement and political-military affairs in the conduct of foreign policy in the Arctic, including programs carried out by other United States Government agencies when such programs pertain to the following matters, to the extent directed by the Secretary of State: (1) National security. (2) Strengthening cooperation among Arctic countries. (3) The promotion of responsible natural resource management and economic development. (4) Protecting the Arctic environment and conserving its biological resources. (5) Arctic indigenous peoples, including by involving them in decisions that affect them. (6) Scientific monitoring and research. (e) Additional duties In addition to the duties and responsibilities specified in subsections (c) and (d), the Ambassador-at-Large for Arctic Affairs shall also carry out such other relevant duties as the Secretary may assign. (f) Definitions In this section: (1) Arctic region The term Arctic region means\u2014 (A) the geographic region north of the 66.56083 parallel latitude north of the equator; (B) all the United States territory north and west of the boundary formed by the Porcupine, Yukon, and Kuskokwim Rivers; (C) all contiguous seas, including the Arctic Ocean and the Beaufort, Bering, and Chukchi Seas; and (D) the Aleutian Chain. (2) Arctic countries The term Arctic countries means the permanent members of the Arctic Council, namely the United States, Canada, Denmark, Iceland, Norway, Sweden, Finland, and Russia. .",
      "versionDate": "2025-10-30",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-05-13",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "3328",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To establish an Ambassador-at-Large for Arctic Affairs.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Arctic and polar regions",
            "updateDate": "2025-12-17T17:23:30Z"
          },
          {
            "name": "Asia",
            "updateDate": "2025-12-17T17:24:18Z"
          },
          {
            "name": "Canada",
            "updateDate": "2025-12-17T17:22:23Z"
          },
          {
            "name": "China",
            "updateDate": "2025-12-17T17:24:02Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-17T17:23:56Z"
          },
          {
            "name": "Denmark",
            "updateDate": "2025-12-17T17:22:32Z"
          },
          {
            "name": "Department of State",
            "updateDate": "2025-12-17T17:21:57Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-12-17T17:22:16Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-12-17T17:24:23Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-12-17T17:22:02Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-12-17T17:22:10Z"
          },
          {
            "name": "Finland",
            "updateDate": "2025-12-17T17:22:56Z"
          },
          {
            "name": "Iceland",
            "updateDate": "2025-12-17T17:22:40Z"
          },
          {
            "name": "Norway",
            "updateDate": "2025-12-17T17:22:46Z"
          },
          {
            "name": "Russia",
            "updateDate": "2025-12-17T17:23:03Z"
          },
          {
            "name": "Sweden",
            "updateDate": "2025-12-17T17:22:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-22T14:04:31Z"
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
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1000is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1000rs.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish an Ambassador-at-Large for Arctic Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:18Z"
    },
    {
      "title": "A bill to establish an Ambassador-at-Large for Arctic Affairs.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T10:56:24Z"
    }
  ]
}
```
