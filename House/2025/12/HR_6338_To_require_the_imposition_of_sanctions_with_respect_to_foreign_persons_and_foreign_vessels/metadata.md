# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6338?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6338
- Title: Stop Illegal Fishing Act
- Congress: 119
- Bill type: HR
- Bill number: 6338
- Origin chamber: House
- Introduced date: 2025-12-01
- Update date: 2026-05-07T08:05:24Z
- Update date including text: 2026-05-07T08:05:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-01 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported by the Yeas and Nays: 47 - 2.
- Latest action: 2025-12-01: Introduced in House

## Actions

- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-01 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported by the Yeas and Nays: 47 - 2.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-01",
    "latestAction": {
      "actionDate": "2025-12-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6338",
    "number": "6338",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M001137",
        "district": "5",
        "firstName": "Gregory",
        "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
        "lastName": "Meeks",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Stop Illegal Fishing Act",
    "type": "HR",
    "updateDate": "2026-05-07T08:05:24Z",
    "updateDateIncludingText": "2026-05-07T08:05:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 47 - 2.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
      "actionDate": "2025-12-01",
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
      "actionDate": "2025-12-01",
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
      "actionDate": "2025-12-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-01",
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
        "item": [
          {
            "date": "2025-12-03T16:18:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-01T17:02:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-01T17:02:15Z",
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "CA"
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
      "sponsorshipDate": "2026-01-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6338ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6338\nIN THE HOUSE OF REPRESENTATIVES\nDecember 1, 2025 Mr. Meeks (for himself and Mrs. Kim ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the imposition of sanctions with respect to foreign persons and foreign vessels that engage in illegal, unreported, and unregulated fishing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Illegal Fishing Act .\n#### 2. Sense of Congress\nIt is the Sense of Congress that\u2014\n**(1)**\nillegal, unreported, and unregulated fishing (referred to in this section as IUU fishing ) is a rising and harmful global trend;\n**(2)**\nthe People\u2019s Republic of China is the primary perpetrator of IUU fishing and the largest exploiter of global fisheries;\n**(3)**\nIUU fishing is a concerning and significant driver of overfishing, thereby threatening fisheries, damaging marine ecosystems, and inhibiting conservation;\n**(4)**\nIUU fishing in another country\u2019s exclusive economic zone violates international law as reflected in the United Nations Convention on the Law of the Sea, undermines the rules-based order, ignores sovereign rights, reinforces excessive maritime claims, exploits finite resources, and unfairly seizes economic access at the expense of coastal states;\n**(5)**\nIUU fishing is often associated with substandard and illicit conditions for crew, including lack of safety controls, illegally low pay, inhumane treatment, and, in some cases, outright forced labor or human trafficking;\n**(6)**\nIUU fishing has a particularly nefarious impact on coastal communities in poor and developing nations that rely on ocean bounties;\n**(7)**\nIUU fishing undermines the economic security of the United States and undermines maritime security around the globe; and\n**(8)**\nthe United States Government should utilize sanctions to deter and prevent IUU fishing.\n#### 3. Sanctions\n##### (a) Sanctions with respect to foreign persons\nThe President shall impose the sanctions described in subsection (e) with respect to any foreign person that knowingly\u2014\n**(1)**\nowns any vessel that engages in IUU fishing;\n**(2)**\nworks as a captain or senior crew member on such a vessel;\n**(3)**\noperates as an entity primarily engaged in IUU fishing; or\n**(4)**\nserves as an officer or senior manager in an entity primarily engaged in IUU fishing.\n##### (b) Sanctions with respect to foreign vessels\nThe President shall impose the sanctions described in subsection (e) with respect to any foreign vessel that engages in IUU fishing.\n##### (c) Report\nNot later than 180 days after the date of enactment of this Act, and annually thereafter for five years, the President shall submit to the appropriate committees a report that\u2014\n**(1)**\ndescribes all efforts to carry out the requirements of subsections (a) and (b); and\n**(2)**\nlists all foreign persons and foreign vessels sanctioned thereunder.\n##### (d) Sanctions program required\nIn carrying out subsection (a) and subsection (b), the President shall direct the creation of an IUU fishing sanctions program.\n##### (e) Sanctions described\nThe sanctions described in this subsection are the following:\n**(1) Asset blocking**\nNotwithstanding the requirements of section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ), the President may exercise of all powers granted to the President by that Act to the extent necessary to block and prohibit all transactions in all property and interests in property of the foreign person or foreign vessel if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Visas, admission, or parole**\n**(A) In general**\nAn alien who the Secretary of State or the Secretary of Homeland Security (or a designee of one of such Secretaries) knows, or has reason to believe, is described in subsection (a) is\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible for a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe issuing consular officer, the Secretary of State, or the Secretary of Homeland Security (or a designee of one of such Secretaries) shall, in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ), revoke any visa or other entry documentation issued to an alien described in subparagraph (A) regardless of when the visa or other entry documentation is issued.\n**(ii) Effect of revocation**\nA revocation under clause (i)\u2014\n**(I)**\nshall take effect immediately; and\n**(II)**\nshall automatically cancel any other valid visa or entry documentation that is in the alien\u2019s possession.\n##### (f) Exceptions\n**(1) Exception to comply with international obligations**\nSanctions under subsection (e)(2) shall not apply with respect to the admission of an alien if admitting or paroling the alien into the United States is necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations.\n**(2) Exception relating to the provision of humanitarian assistance**\nSanctions under this section may not be imposed with respect to transactions or the facilitation of transactions for\u2014\n**(A)**\nthe sale of agricultural commodities, food, medicine, or medical devices;\n**(B)**\nthe provision of humanitarian assistance;\n**(C)**\nfinancial transactions relating to humanitarian assistance; or\n**(D)**\ntransporting goods or services that are necessary to carry out operations relating to humanitarian assistance.\n**(3) Exception for intelligence, law enforcement, and national security activities**\nSanctions under this section shall not apply to any authorized intelligence, law enforcement, or national security activities of the United States.\n**(4) Exception for safety of vessels and crew**\nSanctions under this section shall not apply with respect to a person providing provisions to a vessel otherwise subject to sanctions under this section if such provisions are intended for the safety and care of the crew aboard the vessel, the protection of human life aboard the vessel, or the maintenance of the vessel to avoid any environmental or other significant damage.\n##### (g) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided to the President under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nThe penalties provided for in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) shall apply to a person that violates, attempts to violate, conspires to violate, or causes a violation of regulations promulgated to carry out this section to the same extent that such penalties apply to a person who commits an unlawful act described in section 206(a) of that Act.\n##### (h) Waiver\nThe President may waive the application of sanctions imposed with respect to a foreign person or foreign vessel under this section if the President certifies to the appropriate congressional committees, not later than 15 days before such waiver is to take effect, that the waiver is important to the national security interests of the United States.\n##### (i) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate.\n**(2) Foreign person**\nThe term foreign person means an individual or entity that is not a United States person.\n**(3) Foreign vessel**\nThe term foreign vessel means a vessel of foreign registry or operated under the authority of a foreign country.\n**(4) IUU fishing**\nThe term IUU fishing means illegal, unreported, and unregulated fishing.\n**(5) United States person**\nThe term United States person means\u2014\n**(A)**\na United States citizen;\n**(B)**\na permanent resident alien of the United States;\n**(C)**\nan entity organized under the laws of the United States or of any jurisdiction within the United States, including a foreign branch of such an entity; or\n**(D)**\na person in the United States.",
      "versionDate": "2025-12-01",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-11T15:21:58Z"
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
      "date": "2025-12-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6338ih.xml"
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
      "title": "Stop Illegal Fishing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T11:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Illegal Fishing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-10T11:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the imposition of sanctions with respect to foreign persons and foreign vessels that engage in illegal, unreported, and unregulated fishing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-10T11:03:24Z"
    }
  ]
}
```
