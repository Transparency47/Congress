# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3084?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3084
- Title: Stealthing Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3084
- Origin chamber: House
- Introduced date: 2025-04-29
- Update date: 2025-07-11T08:06:04Z
- Update date including text: 2025-07-11T08:06:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-29: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-29: Introduced in House

## Actions

- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3084",
    "number": "3084",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "T000474",
        "district": "35",
        "firstName": "Norma",
        "fullName": "Rep. Torres, Norma J. [D-CA-35]",
        "lastName": "Torres",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Stealthing Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-11T08:06:04Z",
    "updateDateIncludingText": "2025-07-11T08:06:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-29",
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
          "date": "2025-04-29T14:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NM"
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
      "sponsorshipDate": "2025-04-29",
      "state": "DC"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "IL"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "CT"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MI"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3084ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3084\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2025 Mrs. Torres of California (for herself, Ms. Stansbury , Ms. Norton , Ms. Clarke of New York , Ms. Schakowsky , Mr. Larson of Connecticut , Ms. Tlaib , and Mrs. Cherfilus-McCormick ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo create a civil action for non-consensual sexual protection barrier removal, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stealthing Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nStealthing is a type of sexual violence used to describe non-consensual condom removal during sex.\n**(2)**\nIn October 2021, California became the first State to outlaw stealthing at the State level. This law creates a civil remedy so that victims of stealthing can sue for damages.\n**(3)**\nA 2019 study from Health Psychology reported that almost 10 percent of male participants reported engaging in non-consensual condom removal since the age of 14 years, with an average of 3.62 times and a range of 1\u201321 times.\n**(4)**\nA 2019 study from the Jacobs Institute of Women\u2019s Health found that 12 percent of women have experienced stealthing.\n**(5)**\nA 2018 Australian study from PLoS ONE found that one in three female respondents and one in five gay male respondents have experienced stealthing.\n**(6)**\nStealthing is a grave violation of autonomy, dignity, and trust that is considered emotional and sexual abuse.\n**(7)**\nStealthing exposes victims to physical risks including pregnancy and sexually transmitted diseases.\n**(8)**\nPeople engaging in sexual intercourse have the right to make decisions about whether to use a condom or other sexual protection barrier.\n#### 3. Non-consensual sexual protection barrier removal\n##### (a) Civil action\nAny person may commence a civil action against a person who, in a circumstance described in subsection (b), engages in non-consensual sexual protection barrier removal.\n##### (b) Circumstances described\nFor the purposes of subsection (a), the circumstances described in this subsection are that\u2014\n**(1)**\nthe defendant traveled in interstate or foreign commerce, or traveled using a means, channel, facility, or instrumentality of interstate or foreign commerce, in furtherance of or in connection with the conduct described in subsection (a);\n**(2)**\nthe defendant used a means, channel, facility, or instrumentality of interstate or foreign commerce in furtherance of or in connection with the conduct described in subsection (a);\n**(3)**\na payment of any kind was made, directly or indirectly, in furtherance of or in connection with the conduct described in subsection (a) using any means, channel, facility, or instrumentality of interstate or foreign commerce or in or affecting interstate or foreign commerce;\n**(4)**\nthe defendant transmitted in interstate or foreign commerce any communication relating to or in furtherance of the conduct described in subsection (a) using any means, channel, facility, or instrumentality of interstate or foreign commerce or in or affecting interstate or foreign commerce by any means or in manner, including by computer, mail, wire, or electromagnetic transmission;\n**(5)**\nany sexual protection barrier described has traveled in interstate or foreign commerce and was used to perform the conduct described in subsection (a);\n**(6)**\nthe conduct described in subsection (a) occurred within the special maritime and territorial jurisdiction of the United States, or any territory or possession of the United States; or\n**(7)**\nthe conduct described in subsection (a) otherwise occurred in or affected interstate or foreign commerce.\n##### (c) Penalty\nA person bringing a civil action under subsection (a) may recover compensatory and punitive damages, injunctive and declaratory relief, and such other relief as a court may deem appropriate.\n##### (d) Definitions\nIn this section:\n**(1) Non-consensual sexual protection barrier removal**\nThe term non-consensual sexual protection barrier removal means removal of a sexual protection barrier from a body part, including the genitals, or an object being used by a person for sexual contact with another person without the consent of each person involved in such sexual contact, causing sexual contact between the body parts, including the genitals, or objects being used for sexual contact, and the body of any person engaged in such sexual contact.\n**(2) Sexual protection barrier**\nThe term sexual protection barrier includes a condom, including an internal condom, a dental dam, or any other barrier against sexual fluids during sexual contact.",
      "versionDate": "2025-04-29",
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
        "name": "Law",
        "updateDate": "2025-05-21T13:04:34Z"
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
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3084ih.xml"
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
      "title": "Stealthing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T05:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stealthing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To create a civil action for non-consensual sexual protection barrier removal, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:32Z"
    }
  ]
}
```
