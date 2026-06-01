# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4274?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4274
- Title: WINGS Act
- Congress: 119
- Bill type: S
- Bill number: 4274
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-21T14:33:51Z
- Update date including text: 2026-04-21T14:33:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4274",
    "number": "4274",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "WINGS Act",
    "type": "S",
    "updateDate": "2026-04-21T14:33:51Z",
    "updateDateIncludingText": "2026-04-21T14:33:51Z"
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
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
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
          "date": "2026-03-26T22:59:59Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4274is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4274\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. Sheehy (for himself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo authorize the Secretary of Agriculture to transfer title to certain aircraft and related parts loaned under the Federal Excess Personal Property program to authorized users after a qualifying period of use, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wildfire Investment and Next Generation Stewardship Act or the WINGS Act .\n#### 2. Findings; purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nSince 1956, the Department of Agriculture has operated a Federal Excess Personal Property program through which the Forest Service acquires excess property, primarily from the Department of Defense, and loans such property to State foresters for wildland and rural firefighting purposes.\n**(2)**\nState and local firefighting agencies have successfully used aircraft and related parts obtained through the Federal Excess Personal Property program to protect lives, property, and natural resources for extended periods, often exceeding 10 years.\n**(3)**\nAfter lengthy periods of use, maintenance, and investment by authorized users, uncertainty regarding ownership and disposal authority can create operational and planning difficulties.\n**(4)**\nAuthorizing transfer of title to aircraft and serviceable aircraft parts after a qualifying period of responsible use will improve asset management, reduce administrative burden, and recognize the substantial investment made by State and local agencies in maintaining and operating such property.\n##### (b) Purpose\nThe purpose of this Act is to authorize the Secretary of Agriculture to transfer title to certain aircraft and related parts loaned under the Federal Excess Personal Property program to authorized users that have demonstrated responsible stewardship over a sustained period.\n#### 3. Transfer of title to certain aircraft and related parts loaned under Federal Excess Personal Property program\n##### (a) Definitions\nIn this section:\n**(1) Aircraft**\nThe term aircraft means any fixed wing or rotary wing aircraft, including installed equipment and associated components, that is made available to an authorized user under a Federal Excess Personal Property program.\n**(2) Authorized user**\nThe term authorized user means a State, political subdivision of a State, or other entity that is eligible to receive, and has received, aircraft or serviceable aircraft parts under the Federal Excess Personal Property program.\n**(3) Federal Excess Personal Property program**\nThe term Federal Excess Personal Property program means the program (or a successor program) administered by the Secretary under which aircraft and serviceable aircraft parts are provided to authorized users for the purpose of wildland or rural firefighting.\n**(4) Good standing**\nThe term good standing means, with respect to an authorized user and an aircraft or serviceable aircraft part, that, as determined by the Secretary, the authorized user\u2014\n**(A)**\nis, as of the date of the determination, in compliance with\u2014\n**(i)**\nall applicable statutes, regulations, and written program requirements of the Department of Agriculture relating to property provided under the Federal Excess Personal Property program; and\n**(ii)**\nthe terms and conditions of any agreement or instrument under which the aircraft or serviceable aircraft part was made available to the authorized user;\n**(B)**\nhas timely submitted all required inventories, reports, certifications, and other documentation relating to the aircraft or serviceable aircraft part, as determined by the Secretary;\n**(C)**\nhas not misused, sold, leased, encumbered, transferred, or otherwise disposed of the aircraft or serviceable aircraft part in violation of any applicable requirement or agreement;\n**(D)**\nhas maintained accurate and current inventory records of all serviceable aircraft parts in the possession of the authorized user, whether installed or uninstalled, in accordance with requirements under the Federal Excess Personal Property program; and\n**(E)**\nis not, as of the date of the determination, subject to any suspension, debarment, or other formal enforcement action by the Department of Agriculture that relates to the aircraft, the serviceable aircraft parts, or the Federal Excess Personal Property program.\n**(5) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(6) Serviceable aircraft part**\nThe term serviceable aircraft part means any component, assembly, subassembly, spare part, accessory, support equipment, or other item of equipment, regardless of whether it is currently installed on an aircraft, that is\u2014\n**(A)**\ndesigned for use on, or in support of the maintenance or operation of, an aircraft;\n**(B)**\nmade available to an authorized user under a Federal Excess Personal Property program administered by the Secretary; and\n**(C)**\ndetermined by the authorized user, in accordance with applicable maintenance standards and Federal Excess Personal Property program requirements, to be\u2014\n**(i)**\nin serviceable condition; or\n**(ii)**\ncapable of being restored to serviceable condition through overhaul or maintenance.\n##### (b) Authority To transfer title\n**(1) In general**\nNotwithstanding any other provision of law governing the retention of title to property made available under the Federal Excess Personal Property program, the Secretary may transfer all right, title, and interest of the United States in and to an aircraft or serviceable aircraft part to the authorized user that has received the aircraft or serviceable aircraft part if the requirements of subsection (c) or (d), as applicable, are satisfied.\n**(2) Effect of transfer**\nUpon a transfer under paragraph (1)\u2014\n**(A)**\nthe United States shall have no further ownership interest in the aircraft or serviceable aircraft part; and\n**(B)**\nthe authorized user shall assume full ownership of the aircraft or serviceable aircraft part, subject to\u2014\n**(i)**\nany conditions imposed under subsection (e); and\n**(ii)**\nany applicable Federal law, including laws relating to export controls and national security.\n##### (c) Eligibility for transfer of aircraft\nThe Secretary may approve the transfer of right, title, and interest in and to an aircraft to an authorized user under subsection (b) only if the Secretary determines that\u2014\n**(1)**\nthe authorized user has had continuous possession of the aircraft for not fewer than 10 years beginning on the date the aircraft was first received by the authorized user under the Federal Excess Personal Property program, whether used for operational purposes or as a source of serviceable parts;\n**(2)**\nas of the date of the determination, the authorized user is in good standing with respect to the aircraft; and\n**(3)**\nthe transfer would not be inconsistent with\u2014\n**(A)**\nany statutory limitation or condition governing the original furnishing of the aircraft to the Department of Agriculture by another Federal department or agency; or\n**(B)**\nany applicable national security, export control, or similar restriction, as determined by the Secretary in consultation, as appropriate, with the Secretary of Defense and the heads of any other relevant Federal agencies.\n##### (d) Eligibility for transfer of serviceable aircraft parts\nThe Secretary may approve the transfer of right, title, and interest in and to a serviceable aircraft part to an authorized user under subsection (b) only if the Secretary determines that\u2014\n**(1)**\nthe authorized user\u2014\n**(A)**\nhas had continuous possession of the serviceable aircraft part for not fewer than 5 years beginning on the date the serviceable aircraft part was first received by the authorized user under the Federal Excess Personal Property program; or\n**(B)**\nhas had continuous possession of an aircraft under the Federal Excess Personal Property program for not fewer than 10 years and the serviceable aircraft part was received in support of that aircraft, regardless of when the serviceable aircraft part was received;\n**(2)**\nas of the date of the determination, the authorized user is in good standing with respect to the serviceable aircraft part;\n**(3)**\nthe authorized user has maintained accurate and current inventory records of the serviceable aircraft part in accordance with standards established by the Secretary, including documentation of the condition, location, and intended use of the serviceable aircraft part; and\n**(4)**\nthe transfer would not be inconsistent with\u2014\n**(A)**\nany statutory limitation or condition governing the original furnishing of the serviceable aircraft part to the Department of Agriculture by another Federal department or agency; or\n**(B)**\nany applicable national security, export control, or similar restriction, as determined by the Secretary in consultation, as appropriate, with the Secretary of Defense and the heads of any other relevant Federal agencies.\n##### (e) Conditions on transfers\n**(1) In general**\nAs a condition of approving a transfer under this section, the Secretary may require the authorized user to agree, in such form as the Secretary may prescribe, to 1 or more of the following:\n**(A)**\nThat, for a period not to exceed 5 years beginning on the date of transfer, the authorized user will continue to use any aircraft transferred under this section primarily\u2014\n**(i)**\nfor public purposes consistent with the purposes of the Federal Excess Personal Property program, which may include wildland fire suppression, other emergency response, public safety missions, and training in support of those missions; or\n**(ii)**\nas a source of serviceable aircraft parts to support other aircraft used for the public purposes described in clause (i).\n**(B)**\nThat, for a period not to exceed 3 years beginning on the date of transfer, the authorized user\u2014\n**(i)**\nwill use any serviceable aircraft parts transferred under this section for purposes consistent with the maintenance, repair, overhaul, or operational support of aircraft used for the public purposes described in subparagraph (A)(i); and\n**(ii)**\nwill not use any serviceable aircraft parts transferred under this section for commercial resale or distribution except with the prior written consent of the Secretary.\n**(C)**\nThat, for a period not to exceed 5 years beginning on the date of transfer, the authorized user will not sell, lease, encumber, export, or otherwise dispose of the aircraft or serviceable aircraft parts transferred under this section except\u2014\n**(i)**\nwith the prior written consent of the Secretary; or\n**(ii)**\nin accordance with such conditions as the Secretary may establish by regulation.\n**(D)**\nThat, for a period not to exceed 5 years beginning on the date of transfer, the authorized user will maintain such records relating to the use and disposition of the aircraft or serviceable aircraft parts, and will make such records available to the Secretary upon reasonable request, as the Secretary may require.\n**(2) Modification or waiver**\nThe Secretary may, on a case-by-case basis, modify or waive the application, in whole or in part, of one or more conditions imposed under paragraph (1) if the Secretary determines that such modification or waiver is necessary\u2014\n**(A)**\nto protect public safety;\n**(B)**\nto comply with other applicable Federal law;\n**(C)**\nbecause continued use of the aircraft or serviceable aircraft part by the authorized user is no longer practicable; or\n**(D)**\nto facilitate appropriate maintenance, overhaul, or repair activities.\n##### (f) Application and determination\n**(1) Application**\nAn authorized user seeking a transfer of an aircraft or serviceable aircraft part under this section shall submit to the Secretary an application at such time, in such form, and containing such information as the Secretary may require, including\u2014\n**(A)**\ndocumentation of the date on which the aircraft or serviceable aircraft part was first received or placed into service by the authorized user;\n**(B)**\nif the application relates to one or more serviceable aircraft parts, a complete and current inventory of all such serviceable aircraft parts for which transfer is requested, including information on the condition, location, and intended or actual use of each serviceable aircraft part;\n**(C)**\ninformation sufficient for the Secretary to determine whether the authorized user is in good standing with respect to the aircraft or serviceable aircraft part; and\n**(D)**\nany certifications or other assurances required by the Secretary regarding intended future use and compliance with conditions imposed under subsection (e).\n**(2) Timeline for decision**\nNot later than 180 days after the date on which the Secretary receives a complete application under paragraph (1), the Secretary shall approve or deny the application.\n**(3) Denial**\nIf the Secretary denies an application submitted under paragraph (1), the Secretary shall provide to the authorized user a written notification of the denial that\u2014\n**(A)**\nstates the reasons for the denial; and\n**(B)**\nidentifies, to the extent practicable, any actions the authorized user may take to cure the deficiencies and become eligible for a future transfer with respect to that aircraft, that serviceable aircraft part, or other aircraft or serviceable aircraft parts.\n##### (g) Regulations and guidance\nNot later than 18 months after the date of enactment of this Act, the Secretary shall promulgate such regulations, or issue such revisions to regulations or written guidance, as the Secretary determines to be necessary to carry out this section, including\u2014\n**(1)**\nobjective criteria and procedures for determining whether an authorized user is in good standing;\n**(2)**\nstandards for inventory management, tracking, and reporting of serviceable aircraft parts, including serviceable aircraft parts not installed on an aircraft and serviceable aircraft parts that require overhaul or maintenance before installation;\n**(3)**\nstandards and procedures for evaluating applications and making determinations under subsection (f), including verification of parts inventories and condition assessments;\n**(4)**\nmodel terms and conditions for agreements entered into under subsection (e), with separate or tailored conditions for aircraft and for serviceable aircraft parts; and\n**(5)**\nsafeguards, including any necessary coordination with other Federal departments or agencies, to ensure compliance with statutory limitations and with national security, export control, and similar requirements.\n##### (h) Rule of construction\nNothing in this section shall be construed\u2014\n**(1)**\nto limit any other authority of the Secretary\u2014\n**(A)**\nto transfer title to property;\n**(B)**\nto reclaim property; or\n**(C)**\nto impose conditions on the participation of an authorized user in the Federal Excess Personal Property program; or\n**(2)**\nto affect any law applicable to the original transfer of an aircraft or serviceable aircraft part to the Department of Agriculture by another Federal department or agency.",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-04-21T14:33:50Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4274is.xml"
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
      "title": "WINGS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "WINGS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Wildfire Investment and Next Generation Stewardship Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the Secretary of Agriculture to transfer title to certain aircraft and related parts loaned under the Federal Excess Personal Property program to authorized users after a qualifying period of use, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T03:48:28Z"
    }
  ]
}
```
