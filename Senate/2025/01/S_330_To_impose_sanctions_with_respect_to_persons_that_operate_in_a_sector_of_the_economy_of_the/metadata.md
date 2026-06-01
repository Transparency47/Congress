# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/330?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/330
- Title: CCP IP Act
- Congress: 119
- Bill type: S
- Bill number: 330
- Origin chamber: Senate
- Introduced date: 2025-01-30
- Update date: 2026-04-17T20:17:36Z
- Update date including text: 2026-04-17T20:17:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-30: Introduced in Senate
- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-07-23 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.
- Latest action: 2025-01-30: Introduced in Senate

## Actions

- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-07-23 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-30",
    "latestAction": {
      "actionDate": "2025-01-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/330",
    "number": "330",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "CCP IP Act",
    "type": "S",
    "updateDate": "2026-04-17T20:17:36Z",
    "updateDateIncludingText": "2026-04-17T20:17:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-30",
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
      "actionDate": "2025-01-30",
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
          "date": "2025-07-23T18:30:00Z",
          "name": "Hearings By (full committee)"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-30T18:09:17Z",
          "name": "Referred To"
        }
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s330is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 330\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Mr. Curtis introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo impose sanctions with respect to persons that operate in a sector of the economy of the People\u2019s Republic of China in which the person has engaged in a pattern of significant theft of the intellectual property of a United States person, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Combatting China\u2019s Pilfering of Intellectual Property Act or the CCP IP Act .\n#### 2. Imposition of sanctions related to the theft of intellectual property\n##### (a) In general\nThe President shall impose the sanctions described in subsection (b) with respect to each person described in subsection (c) that the President determines, on or after the date of enactment of this Act, operates in a sector of the economy of the People\u2019s Republic of China in which the person\u2014\n**(1)**\nhas engaged in a pattern of significant theft of the intellectual property of a United States person; or\n**(2)**\nhas received the intellectual property of a United States person through a pattern of significant theft engaged in by other persons.\n##### (b) Sanctions imposed\nThe sanctions described in this subsection are the following:\n**(1) Asset blocking**\nThe exercise of all powers granted to the President by the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in all property and interests in property of a person described in subsection (a) if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Aliens ineligible for visas, admission, or parole**\n**(A) Visas, admission, or parole**\nAn alien described in subsection (a) is\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe issuing consular officer, the Secretary of State, or the Secretary of Homeland Security (or a designee of one of such Secretaries) shall, in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ), revoke any visa or other entry documentation issued to an alien who the Secretary of State or the Secretary of Homeland Security (or a designee of one of such Secretaries) determines is described in subsection (a), regardless of when the visa or other documentation is issued.\n**(ii) Effect of revocation**\nA revocation under clause (i) shall take effect immediately and shall automatically cancel any other valid visa or entry documentation that is in the alien\u2019s possession.\n##### (c) Persons described\nA person described in this subsection is one of the following:\n**(1)**\nAn individual who\u2014\n**(A)**\nis a national of the People\u2019s Republic of China or acting at the direction of a national of the People\u2019s Republic of China or an entity described in paragraph (2); and\n**(B)**\nis not a United States person.\n**(2)**\nAn entity that is\u2014\n**(A)**\norganized under the laws of the People\u2019s Republic of China or of any jurisdiction within the People\u2019s Republic of China;\n**(B)**\nowned or controlled by individuals who are nationals of the People\u2019s Republic of China; or\n**(C)**\nowned or controlled by an entity described in subparagraph (A) that is not a United States person.\n##### (d) Penalties; implementation\n**(1) Penalties**\nA person that violates, attempts to violate, conspires to violate, or causes a violation of subsection (b)(1) or any regulation, license, or order issued to carry out that subsection shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n**(2) Implementation**\nThe President may exercise all authorities provided to the President under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) for purposes of carrying out this section.\n##### (e) Waiver\nThe President may waive the imposition of sanctions under subsection (a) on a case-by-case basis with respect to a person if the President\u2014\n**(1)**\ncertifies to the Committee on Foreign Affairs and the Committee on the Judiciary of the House of Representatives and the Committee on Foreign Relations and the Committee on the Judiciary of the Senate that such waiver is in the national security interests of the United States; and\n**(2)**\nincludes a justification for such certification.\n##### (f) Termination of sanctions\nThe President may terminate sanctions imposed under subsection (a) with respect to a person if the President certifies to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate that such person is no longer engaging in efforts to steal intellectual property of United States persons.\n##### (g) Report required\nNot later than 180 days after the date of the enactment of this Act, the President shall submit to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate a report that specifies each person the President determines meets the criteria described in subsection (a) for the imposition of sanctions.\n##### (h) Definitions\nIn this section:\n**(1) Admitted; alien**\nThe terms admitted and alien have the meanings given those terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) United States person**\nThe term United States person means\u2014\n**(A)**\nan individual who is a United States citizen or an alien lawfully admitted for permanent residence to the United States; or\n**(B)**\nan entity organized under the laws of the United States or of any jurisdiction within the United States.\n#### 3. Restriction on issuance of visas\n##### (a) Restriction\nThe Secretary of State may not issue a visa to, and the Secretary of Homeland Security shall deny entry to the United States of, each of the following:\n**(1)**\nSenior officials in the Chinese Communist Party, including the Politburo, the Central Committee, and each delegate to the 20th National Congress of the Chinese Communist Party.\n**(2)**\nThe spouses and children of the senior officials described in paragraph (1).\n**(3)**\nMembers of the cabinet of the Government of the People\u2019s Republic of China.\n**(4)**\nActive duty members of the People\u2019s Liberation Army of China.\n##### (b) Applicability\nThe restriction under subsection (a) shall not apply for any year in which the President certifies to the Committee on the Judiciary of the House of Representatives and the Committee on the Judiciary of the Senate that the Government of the People\u2019s Republic of China has ceased sponsoring, funding, facilitating, and actively working to support efforts to infringe on the intellectual property rights of citizens and entities of the United States.\n##### (c) Report required\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State shall submit to Congress a report that\u2014\n**(1)**\ndetails the efficacy of visa screening mechanisms to mitigate intellectual property theft by the People\u2019s Republic of China; and\n**(2)**\nincludes a list of research institutions associated with the People\u2019s Liberation Army and the Ministry of State Security of the People\u2019s Republic of China.",
      "versionDate": "2025-01-30",
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
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6447",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "CCP IP Act",
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
            "name": "Asia",
            "updateDate": "2025-08-04T16:24:34Z"
          },
          {
            "name": "China",
            "updateDate": "2025-08-04T16:24:42Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-08-04T16:27:48Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-04T16:24:53Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-08-04T16:25:03Z"
          },
          {
            "name": "Foreign property",
            "updateDate": "2025-08-04T16:25:12Z"
          },
          {
            "name": "Intellectual property",
            "updateDate": "2025-08-04T16:25:19Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-08-04T16:27:14Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2025-08-04T16:25:27Z"
          },
          {
            "name": "Visas and passports",
            "updateDate": "2025-08-04T16:25:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-03-06T16:03:50Z"
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
      "date": "2025-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s330is.xml"
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
      "title": "CCP IP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CCP IP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Combatting China\u2019s Pilfering of Intellectual Property Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to impose sanctions with respect to persons that operate in a sector of the economy of the People's Republic of China in which the person has engaged in a pattern of significant theft of the intellectual property of a United States person, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:31Z"
    }
  ]
}
```
