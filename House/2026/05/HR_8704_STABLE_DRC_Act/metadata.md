# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8704?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8704
- Title: STABLE DRC Act
- Congress: 119
- Bill type: HR
- Bill number: 8704
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-12T19:45:26Z
- Update date including text: 2026-05-12T19:45:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-07 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-07 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8704",
    "number": "8704",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "O000176",
        "district": "2",
        "firstName": "Johnny",
        "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
        "lastName": "Olszewski",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "STABLE DRC Act",
    "type": "HR",
    "updateDate": "2026-05-12T19:45:26Z",
    "updateDateIncludingText": "2026-05-12T19:45:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
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
      "actionDate": "2026-05-07",
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
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:02:20Z",
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
          "date": "2026-05-07T13:02:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8704ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8704\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Olszewski introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo impose sanctions with respect to any foreign person that violates or knowingly undermines the Washington Accords.\n#### 1. Short title\nThis Act may be cited as the Sanctioning Threats and Aggression to Bolster Lasting Enforcement and Disrupt Regional Conflict Act or STABLE DRC Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe Rwandan Defense Forces have provided sustained military support for the March 23rd Movement\u2019s (M23) ongoing revolt in the Democratic Republic of the Congo\u2019s North and South Kivu provinces.\n**(2)**\nThe armed forces of the Democratic Republic of the Congo continue to support the Democratic Forces for the Liberation of Rwanda (FDLR), an armed group whose founders took part in the 1994 Rwandan genocide.\n**(3)**\nBoth the FDLR and M23 have committed numerous war crimes and human rights abuses. This includes forcibly recruiting children into their ranks and engaging in ethnic cleansing, rape, and summary executions.\n**(4)**\nThe June 2025 Peace Agreement between the Democratic Republic of the Congo and Rwanda (in this Act referred to as the Washington Accords ) stipulates that each party will respect the other\u2019s sovereignty and territorial integrity, as well as refrain from engaging in hostile acts that threaten the peace and security of the other signatory state.\n#### 3. Statement of policy\nIt shall be the policy of the United States Government\u2014\n**(1)**\nto recognize the independence, sovereignty, and territorial integrity of the Democratic Republic of the Congo and Rwanda;\n**(2)**\nto regard the conflict in eastern Democratic Republic of the Congo as a direct threat to regional peace and stability, as well as to United States strategic interests in Central Africa; and\n**(3)**\nto use sanctions as a tool to support the Washington Accords and to fully end the conflict between the Democratic Republic of the Congo, M23, and Rwanda.\n#### 4. Sanctions\n##### (a) Authorization\nBeginning on the date of the enactment of this Act, the President is authorized to impose the sanctions described in subsection (b) with respect to any foreign person that violates or knowingly undermines the Washington Accords.\n##### (b) Sanctions described\nThe sanctions described in this subsection are the following: \u2014\n**(1) Asset blocking**\nNotwithstanding the requirements of section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ), the President may exercise of all powers granted to the President by that Act to the extent necessary to block and prohibit all transactions in all property and interests in property of the foreign person if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Aliens inadmissible for visas, admission, or parole**\n**(A) Visas, admission, or parole**\nIn the case of an alien subject to sanctions pursuant to subsection (a), the alien is\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe visa or other entry documentation of an alien described in subparagraph (A) shall be revoked, regardless of when such visa or other entry documentation was issued.\n**(ii) Immediate effect**\nA revocation under clause (i) shall\u2014\n**(I)**\ntake effect in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ); and\n**(II)**\ncancel any other valid visa or entry documentation that is in the alien\u2019s possession.\n##### (c) Exceptions\n**(1) Exception to comply with international obligations**\nSanctions under subsection (b)(2) shall not apply with respect to the admission of an alien if admitting or paroling the alien into the United States is necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations.\n**(2) Exception relating to the provision of humanitarian assistance**\nSanctions under this section may not be imposed with respect to transactions or the facilitation of transactions for\u2014\n**(A)**\nthe sale of agricultural commodities, food, medicine, or medical devices;\n**(B)**\nthe provision of humanitarian assistance;\n**(C)**\nfinancial transactions relating to humanitarian assistance; or\n**(D)**\ntransporting goods or services that are necessary to carry out operations relating to humanitarian assistance.\n**(3) Exception for intelligence, law enforcement, and national security activities**\nSanctions under this section shall not apply to any authorized intelligence, law enforcement, or national security activities of the United States.\n##### (d) Sanctions program\n**(1) In general**\nThe President shall establish or direct the establishment of a program to carry out the authority under this section.\n**(2) Existing authorities**\nThe President is authorized to impose sanctions under this section with respect to any foreign person described in subsection (a) that is also subject to sanctions under any other provision of law.\n##### (e) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided to the President under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nThe penalties provided for in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) shall apply to a person that violates, attempts to violate, conspires to violate, or causes a violation of regulations promulgated to carry out this section to the same extent that such penalties apply to a person who commits an unlawful act described in section 206(a) of that Act.\n##### (f) Sunset\nThe authority to impose sanctions under this section shall terminate on the date that is seven years after the date of the enactment of this Act.\n##### (g) Definitions\nIn this section\u2014\n**(1)**\nthe term \u201cappropriate congressional committees\u201d means the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate;\n**(2)**\nthe term \u201cforeign person\u201d means an individual or entity that is not a United States person; and\n**(3)**\nthe term \u201cUnited States person\u201d means\u2014\n**(A)**\na United States citizen;\n**(B)**\na permanent resident alien of the United States;\n**(C)**\nan entity organized under the laws of the United States or of any jurisdiction within the United States, including a foreign branch of such an entity; or\n**(D)**\na person in the United States.",
      "versionDate": "2026-05-07",
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
        "updateDate": "2026-05-12T19:45:26Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8704ih.xml"
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
      "title": "STABLE DRC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T08:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STABLE DRC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T08:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sanctioning Threats and Aggression to Bolster Lasting Enforcement and Disrupt Regional Conflict Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T08:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To impose sanctions with respect to any foreign person that violates or knowingly undermines the Washington Accords.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T08:18:46Z"
    }
  ]
}
```
