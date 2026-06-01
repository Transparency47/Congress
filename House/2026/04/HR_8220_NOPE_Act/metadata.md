# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8220?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8220
- Title: NOPE Act
- Congress: 119
- Bill type: HR
- Bill number: 8220
- Origin chamber: House
- Introduced date: 2026-04-09
- Update date: 2026-04-21T01:37:35Z
- Update date including text: 2026-04-21T01:37:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-09: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-09: Introduced in House

## Actions

- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-09",
    "latestAction": {
      "actionDate": "2026-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8220",
    "number": "8220",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "L000606",
        "district": "16",
        "firstName": "George",
        "fullName": "Rep. Latimer, George [D-NY-16]",
        "lastName": "Latimer",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "NOPE Act",
    "type": "HR",
    "updateDate": "2026-04-21T01:37:35Z",
    "updateDateIncludingText": "2026-04-21T01:37:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-09",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-09",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-09",
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
          "date": "2026-04-09T15:30:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-09T15:30:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8220ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8220\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2026 Mr. Latimer introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo nullify Iran-related General License U, Authorizing the Delivery and Sale of Crude Oil and Petroleum Products of Iranian Origin Loaded on Vessels as of March 20, 2026 , and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Oil Profiteering to Enrich Iran Act or NOPE Act .\n#### 2. Nullification of Iran-related General License U\n##### (a) In general\nEffective beginning on the date of the enactment of this Act, Iran-related General License U, Authorizing the Delivery and Sale of Crude Oil and Petroleum Products of Iranian Origin Loaded on Vessels as of March 20, 2026 , issued by the Office of Foreign Assets Control of the Department of the Treasury, shall have no force or effect.\n##### (b) Future licenses\nThe Secretary of Treasury may not authorize any transactions otherwise prohibited by law that are ordinarily incident and necessary to the sale, delivery, or offloading of crude oil or petroleum products of Iran.\n#### 3. Imposition of sanctions\n##### (a) In general\nNot later than 30 days after the date of the enactment of this Act, the President shall impose the sanctions described in subsection (b) with respect to any Iranian person that engages in the following:\n**(1)**\nOil and gas extraction.\n**(2)**\nOil and gas refinement or production.\n**(3)**\nMaritime transportation of oil and gas or other petroleum products.\n##### (b) Sanctions described\nThe sanctions described in this subsection are the following:\n**(1) Asset blocking**\nNotwithstanding the requirements of section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ), the President may exercise all powers granted to the President by that Act to the extent necessary to block and prohibit all transactions in all property and interests in property of the person if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Visas, admission, or parole**\n**(A) In general**\nAn alien who the Secretary of State or the Secretary of Homeland Security (or a designee of one of such Secretaries) knows, or has reason to believe, is described in subsection (a) is\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible for a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe issuing consular officer, the Secretary of State, or the Secretary of Homeland Security (or a designee of one of such Secretaries) shall, in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ), revoke any visa or other entry documentation issued to an alien described in subparagraph (A) regardless of when the visa or other entry documentation is issued.\n**(ii) Effect of revocation**\nA revocation under clause (i)\u2014\n**(I)**\nshall take effect immediately; and\n**(II)**\nshall automatically cancel any other valid visa or entry documentation that is in the alien\u2019s possession.\n##### (c) Exceptions\n**(1) Exception to comply with international obligations**\nSanctions under subsection (b)(2) shall not apply with respect to the admission of an alien if admitting or paroling the alien into the United States is necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations.\n**(2) Exception relating to the provision of humanitarian assistance**\nSanctions under this section may not be imposed with respect to transactions or the facilitation of transactions for\u2014\n**(A)**\nthe sale of agricultural commodities, food, medicine, or medical devices;\n**(B)**\nthe provision of humanitarian assistance;\n**(C)**\nfinancial transactions relating to humanitarian assistance; or\n**(D)**\ntransporting goods or services that are necessary to carry out operations relating to humanitarian assistance.\n**(3) Exception for intelligence, law enforcement, and national security activities**\nSanctions under this section shall not apply to any authorized intelligence, law enforcement, or national security activities of the United States.\n##### (d) Classified information\nIn any judicial review of a determination made under this section, if the determination was based on classified information (as defined in section 1(a) of the Classified Information Procedures Act) such information may be submitted to the reviewing court ex parte and in camera. This subsection does not confer or imply any right to judicial review.\n##### (e) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided to the President under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nThe penalties provided for in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) shall apply to a person that violates, attempts to violate, conspires to violate, or causes a violation of regulations promulgated to carry out this section to the same extent that such penalties apply to a person who commits an unlawful act described in section 206(a) of that Act.\n#### 4. Report on Iranian oil\n##### (a) In general\nNot later than 30 days after the date of enactment of this Act, and every 60 days thereafter for three years, the Secretary of State in consultation with the heads of other Federal departments and agencies as appropriate, shall submit to the appropriate congressional committees a report on the impact of the closure of the Strait of Hormuz on Iranian oil.\n##### (b) Elements\nEach report under subsection (a) shall include an analysis of the impact of Iran-related General License U, Authorizing the Delivery and Sale of Crude Oil and Petroleum Products of Iranian Origin Loaded on Vessels as of March 20, 2026 , issued by the Office of Foreign Assets Control of the Department of the Treasury and any extensions or successors thereof on the following:\n**(1)**\nThe volume and sale price of Iranian crude and refined oil product exports.\n**(2)**\nThe revenue earned by the Government of the Iran or state-affiliated or state-owned entities through exports of oil products, including the premium earned on Iranian oil as a result of the closure of the Strait of Hormuz and the subsequent fallout thereof.\n**(3)**\nIranian oil production levels as of April 2026.\n##### (c) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Relations and the Committee on Energy and Natural Resources of the Senate; and\n**(2)**\nthe Committee on Foreign Affairs and the Committee on Energy and Commerce of the House of Representatives.",
      "versionDate": "2026-04-09",
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
        "updateDate": "2026-04-21T01:37:34Z"
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
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8220ih.xml"
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
      "title": "NOPE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T06:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NOPE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T06:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Oil Profiteering to Enrich Iran Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T06:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To nullify Iran-related General License U, \"Authorizing the Delivery and Sale of Crude Oil and Petroleum Products of Iranian Origin Loaded on Vessels as of March 20, 2026\", and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T06:18:46Z"
    }
  ]
}
```
