# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/286?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/286
- Title: Of inquiry requesting the President to transmit certain documents relating to the dangerous, unaccountable use of AI by the United States DOGE Service to jeopardize the private information and essential services of the American people.
- Congress: 119
- Bill type: HRES
- Bill number: 286
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2025-06-03T15:52:09Z
- Update date including text: 2025-06-03T15:52:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-04-01 - IntroReferral: Sponsor introductory remarks on measure. (CR H1386)
- 2025-04-01 - IntroReferral: Submitted in House
- 2025-04-01 - IntroReferral: Submitted in House
- 2025-04-30 - Committee: Committee Consideration and Mark-up Session Held
- Latest action: 2025-04-01: Submitted in House

## Actions

- 2025-04-01 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-04-01 - IntroReferral: Sponsor introductory remarks on measure. (CR H1386)
- 2025-04-01 - IntroReferral: Submitted in House
- 2025-04-01 - IntroReferral: Submitted in House
- 2025-04-30 - Committee: Committee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/286",
    "number": "286",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001218",
        "district": "1",
        "firstName": "Melanie",
        "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
        "lastName": "Stansbury",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Of inquiry requesting the President to transmit certain documents relating to the dangerous, unaccountable use of AI by the United States DOGE Service to jeopardize the private information and essential services of the American people.",
    "type": "HRES",
    "updateDate": "2025-06-03T15:52:09Z",
    "updateDateIncludingText": "2025-06-03T15:52:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H1386)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
            "date": "2025-04-30T15:13:56Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-01T14:03:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "VA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "DC"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "IL"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MD"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "OH"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MI"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "FL"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "PA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "TX"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "TX"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "WA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "VA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "AZ"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MO"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres286ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 286\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Ms. Stansbury (for herself, Mr. Connolly , Ms. Norton , Mr. Lynch , Mr. Krishnamoorthi , Mr. Khanna , Mr. Mfume , Ms. Brown , Ms. Tlaib , Mr. Garcia of California , Mr. Frost , Ms. Lee of Pennsylvania , Mr. Casar , Ms. Crockett , Ms. Randall , Mr. Subramanyam , Ms. Ansari , Mr. Bell , Ms. Simon , Mr. Min , and Ms. Pressley ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nOf inquiry requesting the President to transmit certain documents relating to the dangerous, unaccountable use of AI by the United States DOGE Service to jeopardize the private information and essential services of the American people.\nThat the President is requested to transmit, to the extent that such documents are in the possession of the President, to the House of Representatives, not later than 14 days after the adoption of this resolution, in a complete and unredacted form, a copy of any document, record, report, memorandum, correspondence, or other communication that refers or relates to the following:\n**(1)**\nAny artificial intelligence (AI) technology newly deployed or used at a Federal agency, by or at the direction of Elon Musk or an individual associated with the United States DOGE Service or DOGE, from January 20, 2025, to present, including any associated System of Records Notice, Privacy Impact Assessment, or Authorization to Operate.\n**(2)**\nThe Federal data and sources of Federal data fed into such AI technology, including any reference as to whether such data contains the sensitive, personally identifiable information of American citizens.\n**(3)**\nAll individuals involved in both the policy decisions and technical planning associated with the feeding of sensitive Federal data to AI technology from January 20, 2025, to present, including\u2014\n**(A)**\nindividuals involved in plans to use AI technology to cut payments\u2014\n**(i)**\nto Americans; or\n**(ii)**\nassociated with programs for Americans; and\n**(B)**\nindividuals involved in plans to collect and feed government contract data through AI software, including any concerns raised or steps taken to mitigate Elon Musk\u2019s related conflicts of interest.\n**(4)**\nAny concerns raised by Federal workers that such actions by the Trump Administration violated the Privacy Act and the security of Americans\u2019 private information.\n**(5)**\nAny concerns raised by Federal workers that such actions by the Trump Administration violated the Advancing American AI Act by failing to publicly disclose current and planned AI use cases to ensure transparency for the American people.\n**(6)**\nAny lists of Federal expenditures, programs, or personnel identified by AI software for freezes or cuts.\n**(7)**\nAny analyses undertaken by any individual to determine which of such AI-identified expenditures, programs, or personnel to freeze or cut.\n**(8)**\nAny communication or correspondence regarding\u2014\n**(A)**\nthe legality of such freezes or cuts;\n**(B)**\nthe harms to the American people of such freezes or cuts; and\n**(C)**\nwhether employees of DOGE or their associates believe that legality or harm to the American people are important considerations in their actions.\n**(9)**\nAll individuals who managed or accessed Federal data in the process of feeding it through AI technology, including whether such individuals were Federal workers at the time of their data management or access and, if so\u2014\n**(A)**\nunder what authority they were hired; and\n**(B)**\nwhat background investigation and clearance processes they underwent as part of the hiring process.\n**(10)**\nAll records, logs, code, certificates, and configurations for all Federal IT assets, databases, or repositories accessed by employees of DOGE in training or deploying new AI software.",
      "versionDate": "2025-04-01",
      "versionType": "IH"
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-06-03T15:51:47Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-06-03T15:51:55Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-03T15:51:36Z"
          },
          {
            "name": "Congressional-executive branch relations",
            "updateDate": "2025-06-03T15:51:24Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-03T15:52:09Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-03T15:51:30Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-06-03T15:51:41Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2025-06-03T15:52:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-22T18:21:55Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres286ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Of inquiry requesting the President to transmit certain documents relating to the dangerous, unaccountable use of AI by the United States DOGE Service to jeopardize the private information and essential services of the American people.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Of inquiry requesting the President to transmit certain documents relating to the dangerous, unaccountable use of AI by the United States DOGE Service to jeopardize the private information and essential services of the American people.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:58:27Z"
    }
  ]
}
```
