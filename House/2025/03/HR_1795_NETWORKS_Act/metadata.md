# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1795?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1795
- Title: NETWORKS Act
- Congress: 119
- Bill type: HR
- Bill number: 1795
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2025-07-01T08:05:23Z
- Update date including text: 2025-07-01T08:05:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1795",
    "number": "1795",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "H001085",
        "district": "6",
        "firstName": "Chrissy",
        "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
        "lastName": "Houlahan",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "NETWORKS Act",
    "type": "HR",
    "updateDate": "2025-07-01T08:05:23Z",
    "updateDateIncludingText": "2025-07-01T08:05:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "AL"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "IA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1795ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1795\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Ms. Houlahan (for herself and Mr. Strong ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo impose sanctions with respect to foreign telecommunications companies engaged in economic or industrial espionage against United States persons, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Neutralizing Emerging Threats from Wireless OEMs Receiving direction from Kleptocracies and Surveillance states Act or the NETWORKS Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nsecure telecommunications networks, both domestically and within partner and allied nations, are important to the national security of the United States;\n**(2)**\nthe risks posed by untrusted telecommunications vendors, particularly those based in the People\u2019s Republic of China, to communications, data security, and the viability of networks outweigh any potential benefits; and\n**(3)**\nthe United States Government should use the tools of economic statecraft to promote secure telecommunications networks.\n#### 3. Imposition of sanctions with respect to economic or industrial espionage by foreign telecommunications companies\n##### (a) In general\nOn and after the date that is 90 days after the date of the enactment of this Act, the President shall exercise all of the powers granted to the President under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all significant transactions in property and interests in property of a foreign person described in subsection (b) if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n##### (b) Foreign persons described\nA foreign person is described in this subsection if the President determines that the person, on or after the date of the enactment of this Act\u2014\n**(1)**\nproduces fifth or future generation telecommunications technology; and\n**(2)**\nconducts business relating to such telecommunications technology in a manner contrary to the United States\u2019 national security interests.\n##### (c) Exceptions\n**(1) Exception for intelligence activities**\nSanctions under this section shall not apply to any activity subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ) or any authorized intelligence activities of the United States.\n**(2) Exception relating to the provision of humanitarian assistance**\nSanctions under this section may not be imposed with respect to transactions or the facilitation of transactions for\u2014\n**(A)**\nthe sale of agricultural commodities, food, medicine, or medical devices;\n**(B)**\nthe provision of humanitarian assistance;\n**(C)**\nfinancial transactions relating to humanitarian assistance; or\n**(D)**\ntransporting goods or services that are necessary to carry out operations relating to humanitarian assistance.\n##### (d) Waiver\nThe President may waive the application of sanctions under this section with respect to a foreign person for renewable periods of not more than 90 days each if the President determines and reports to Congress that such a waiver is vital to the national security interests of the United States.\n##### (e) Implementation; penalties\n**(1) Implementation**\nThe President may exercise the authorities provided to the President under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to the extent necessary to carry out this section.\n**(2) Penalties**\nA person that violates, attempts to violate, conspires to violate, or causes a violation of subsection (a) or any regulation, license, or order issued to carry out that subsection shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n##### (f) Definitions\n**(1) In general**\nIn this section:\n**(A) Fifth or future generation telecommunications technology**\nThe term fifth or future generation telecommunications technology means telecommunications technology that conforms to the technical standards followed by the telecommunications industry for telecommunications technology that is commonly known in the industry as fifth generation or future generation technology.\n**(B) Foreign person**\nThe term foreign person means any person that is not a United States person.\n**(C) Knowingly**\nThe term knowingly , with respect to conduct, a circumstance, or a result, means that a person has actual knowledge, or should have known, of the conduct, the circumstance, or the result.\n**(D) Person**\nThe term person means an individual or entity.\n**(E) United States person**\nThe term United States person means\u2014\n**(i)**\na United States citizen or an alien lawfully admitted for permanent residence to the United States; or\n**(ii)**\nan entity organized under the laws of the United States or any jurisdiction within the United States, including a foreign branch of such an entity.\n**(F) Untrusted telecommunications vendor**\nThe term \u201cuntrusted telecommunications vendor\u201d has the meaning given to the term \u201ccovered communications equipment or service\u201d in section 9 of the Secure and Trusted Communications Network Act of 2019 ( 47 U.S.C. 1608 ).\n**(2) Determination of significance**\nFor the purposes of this section, in determining if transactions are significant, the President may consider the totality of the facts and circumstances, including factors similar to the factors set forth in section 561.404 of title 31, Code of Federal Regulations (or any corresponding similar regulation or ruling).\n**(3) Rule of construction**\nFor purposes of this section, a transaction shall not be construed to include\u2014\n**(A)**\nparticipation in an international standards-setting body or the activities of such a body; or\n**(B)**\na transaction involving existing third or fourth generation telecommunications networks.",
      "versionDate": "2025-03-03",
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
        "name": "International Affairs",
        "updateDate": "2025-05-08T16:37:06Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1795ih.xml"
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
      "title": "NETWORKS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T10:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NETWORKS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Neutralizing Emerging Threats from Wireless OEMs Receiving direction from Kleptocracies and Surveillance states Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To impose sanctions with respect to foreign telecommunications companies engaged in economic or industrial espionage against United States persons, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T10:18:33Z"
    }
  ]
}
```
