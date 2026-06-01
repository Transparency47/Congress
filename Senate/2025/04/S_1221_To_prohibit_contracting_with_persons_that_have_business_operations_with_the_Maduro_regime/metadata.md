# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1221?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1221
- Title: BOLIVAR Act
- Congress: 119
- Bill type: S
- Bill number: 1221
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2025-09-17T11:03:17Z
- Update date including text: 2025-09-17T11:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1221",
    "number": "1221",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "BOLIVAR Act",
    "type": "S",
    "updateDate": "2025-09-17T11:03:17Z",
    "updateDateIncludingText": "2025-09-17T11:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T16:25:28Z",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "TX"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "TN"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1221is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1221\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Mr. Scott of Florida (for himself, Mr. Cruz , and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit contracting with persons that have business operations with the Maduro regime, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Banning Operations and Leases with the Illegitimate Venezuelan Authoritarian Regime Act or the BOLIVAR Act .\n#### 2. Prohibition on contracting with persons that have business operations with the Maduro regime\n##### (a) Prohibition\nExcept as provided in subsections (b), (c), and (d), the head of an executive agency may not enter into a contract for the procurement of goods or services with any person that the head of an executive agency determines, with the concurrence of the Secretary of State, knowingly engages in significant business operations with an authority of the Government of Venezuela that is not recognized as the legitimate Government of Venezuela by the United States.\n##### (b) Exceptions\n**(1) In general**\nThe prohibition under subsection (a) does not apply to a contract that the Secretary of State determines\u2014\n**(A)**\nis necessary\u2014\n**(i)**\nfor purposes of providing humanitarian assistance to the people of Venezuela;\n**(ii)**\nfor purposes of providing disaster relief and other urgent life-saving measures; or\n**(iii)**\nto carry out noncombatant evacuations; or\n**(B)**\nis in the national security interests of the United States.\n**(2) Support for United States Government activities**\nThe prohibition in subsection (a) shall not apply to contracts that support United States Government activities in Venezuela, including those necessary for the maintenance of United States Government facilities in Venezuela, or to contracts with international organizations.\n**(3) Notification requirement**\nThe Secretary of State shall notify the appropriate congressional committees of any contract entered into on the basis of an exception provided for under paragraph (1).\n##### (c) Office of foreign assets control licenses\nThe prohibition in subsection (a) does not apply to a person that has a valid license to operate in Venezuela issued by the Office of Foreign Assets Control.\n##### (d) American diplomatic mission in Venezuela\nThe prohibition in subsection (a) does not apply to contracts related to the operation and maintenance of the United States Government\u2019s consular offices and diplomatic posts in Venezuela.\n##### (e) Waiver\nThe Secretary of State may waive the requirements of subsection (a) if the Secretary of State determines that to do so is in the national interest of the United States.\n##### (f) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means the Committee on Homeland Security and Governmental Affairs and the Committee on Foreign Relations of the Senate and the Committee on Homeland Security and the Committee on Foreign Affairs of the House of Representatives.\n**(2) Business operations**\nThe term business operations means engaging in commerce in any form, including acquiring, developing, maintaining, owning, selling, possessing, leasing, or operating equipment, facilities, personnel, products, services, personal property, real property, or any other apparatus of business or commerce.\n**(3) Executive agency**\nThe term executive agency has the meaning given the term in section 133 of title 41, United States Code.\n**(4) Government of Venezuela**\n**(A)**\nThe term Government of Venezuela includes the government of any political subdivision of Venezuela, and any agency or instrumentality of the Government of Venezuela.\n**(B)**\nFor purposes of subparagraph (A), the term agency or instrumentality of the Government of Venezuela means an agency or instrumentality of a foreign state as defined in section 1603(b) of title 28, United States Code, with each reference in such section to a foreign state deemed to be a reference to Venezuela .\n**(5) Person**\nThe term person means\u2014\n**(A)**\na natural person, corporation, company, business association, partnership, society, trust, or any other nongovernmental entity, organization, or group;\n**(B)**\nany governmental entity or instrumentality of a government; and\n**(C)**\nany successor, subunit, parent entity, or subsidiary of, or any entity under common ownership or control with, any entity described in subparagraph (A) or (B).\n##### (g) Term of applicability\nThis section shall apply with respect to any contract entered into during the three-year period beginning on the date of the enactment of this Act.",
      "versionDate": "2025-04-01",
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
        "updateDate": "2025-05-14T16:42:25Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1221is.xml"
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
      "title": "BOLIVAR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-17T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BOLIVAR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Banning Operations and Leases with the Illegitimate Venezuelan Authoritarian Regime Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit contracting with persons that have business operations with the Maduro regime, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:48:27Z"
    }
  ]
}
```
