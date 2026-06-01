# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4829?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4829
- Title: Transnational Repression Policy Act
- Congress: 119
- Bill type: HR
- Bill number: 4829
- Origin chamber: House
- Introduced date: 2025-08-01
- Update date: 2026-03-05T09:07:02Z
- Update date including text: 2026-03-05T09:07:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-01 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-08-01: Introduced in House

## Actions

- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-01 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4829",
    "number": "4829",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S000522",
        "district": "4",
        "firstName": "Christopher",
        "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
        "lastName": "Smith",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Transnational Repression Policy Act",
    "type": "HR",
    "updateDate": "2026-03-05T09:07:02Z",
    "updateDateIncludingText": "2026-03-05T09:07:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-01",
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
      "actionDate": "2025-08-01",
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
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T14:05:20Z",
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
          "date": "2025-08-01T14:05:15Z",
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
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "DC"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "MI"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4829ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4829\nIN THE HOUSE OF REPRESENTATIVES\nAugust 1, 2025 Mr. Smith of New Jersey (for himself and Mr. McGovern ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo address transnational repression by foreign governments against private individuals, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Transnational Repression Policy Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Statement of policy.\nSec. 3. Defined term.\nSec. 4. Interagency strategy.\nSec. 5. Training.\nSec. 6. Department of Homeland Security and Department of Justice efforts to combat transnational repression in the United States.\n#### 2. Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nto protect persons within the United States, and United States nationals who are outside of the United States, from actions by foreign governments, or individuals acting on behalf of foreign governments, that violate internationally recognized human rights;\n**(2)**\nto encourage cooperation with like-minded foreign partners to mitigate transnational repression; and\n**(3)**\nto pursue criminal prosecutions, as appropriate, and undertake other steps, such as facilitating mutual legal assistance, in accordance with United States law, to hold foreign governments and individuals acting on behalf of foreign governments, including unregistered foreign agents, accountable for engaging in transnational repression.\n#### 3. Defined term\nIn this Act, the term transnational repression refers to a range of tactics deployed by a foreign government, or agents or proxies of a foreign government, to reach beyond their borders to intimidate, silence, harass, coerce, or harm individuals, such as political dissidents, activists, journalists, political opponents, religious and ethnic minority groups, international students, and members of diaspora and exile communities.\n#### 4. Interagency strategy\n##### (a) In general\nNot later than 270 days after the date of the enactment of this Act, the Secretary of State, in coordination with the heads of other appropriate Federal departments and agencies, shall submit a report to the Committee on Foreign Relations of the Senate , the Committee on the Judiciary of the Senate , the Committee on Foreign Affairs of the House of Representatives , and the Committee on the Judiciary of the House of Representatives that contains a United States strategy\u2014\n**(1)**\nto increase international awareness of transnational repression;\n**(2)**\nto raise the costs borne by governments engaging in transnational repression by holding such governments accountable and protecting targeted individuals and groups; and\n**(3)**\nto increase collaboration and coordination concerning transnational repression with like-minded allies and partners and in multilateral venues and international organizations.\n##### (b) Matters To be included\n**(1) Diplomacy**\nThe strategy required under subsection (a) shall include\u2014\n**(A)**\na strategy for advancing joint initiatives in multilateral and international organizations to expand awareness, accountability, and best practices to mitigate and build capacity to counter transnational repression;\n**(B)**\na plan for establishing or strengthening regional and international coalitions to monitor and respond to cases of transnational repression, including reprisals faced by human rights defenders and other activists for engaging at multilateral organizations, such as the United Nations;\n**(C)**\nan analysis of the advantages and disadvantages of the designation of a special rapporteur for transnational repression appointed by the Secretary-General of the United Nations;\n**(D)**\na plan for engaging with foreign diplomatic or consular missions in the United States whose personnel abuse intimidate, threaten, attack, or undermine the human rights and fundamental freedoms of exiles and members of diasporas in the United States; and\n**(E)**\na description of the public affairs and public diplomacy efforts, including at multilateral institutions and international exchanges, to be used to draw critical attention to, and oppose acts of, transnational repression.\n**(2) Assistance programming**\nThe strategy shall include sufficient funding for civil society and nongovernmental organizations that support victims of transnational repression and conduct research and analysis of global trends and incidents of transnational repression.\n**(3) Law enforcement in the United States**\nThe strategy shall\u2014\n**(A)**\nconsider updates to United States law to address tactics of transnational repression, including\u2014\n**(i)**\nthe criminalization of gathering information about private individuals in diaspora and exile communities on behalf of, or enabling the ability of, a foreign government to harass, intimidate, or harm an individual due to membership in such a community; and\n**(ii)**\nthe expansion of the definition of foreign agents under the Foreign Registrations Act of 1938 ( 22 U.S.C. 611 et seq. ) and section 951 of title 18, United States Code;\n**(B)**\ncoordinate between the Federal Bureau of Investigation, the Department of State, the Department of Homeland Security, United States intelligence agencies, and domestic law enforcement agencies in partner countries, including options for countering the use of surveillance technology and export licensing policy in transnational repression;\n**(C)**\nconsider unintended negative impacts of expanded legal authorities on the civil liberties of communities targeted by transnational repression, taking into account the views of affected communities;\n**(D)**\ndevelop outreach strategies to connect law enforcement and local municipal officials with targeted diaspora communities to ensure individuals who are vulnerable to transnational repression are aware of the Federal and local resources available without putting them at further risk, including policy and programmatic responses based on input from such communities; and\n**(E)**\nexamine and review the legality of foreign governments establishing overseas police service stations, or equivalent facilities, to monitor members of the diaspora.\n##### (c) Additional matters To be included\nIn addition to the matters set forth in subsection (b), the report required under subsection (a) should include\u2014\n**(1)**\nto the extent practicable, information regarding\u2014\n**(A)**\nthe governments that perpetrate transnational repression;\n**(B)**\ncountries in which incidents of transnational repression are prevalent;\n**(C)**\ngovernments that are complicit in aiding transnational repression;\n**(D)**\nindividuals, whether United States citizens or foreign nationals, who are complicit in transnational repression as agents or proxies of a foreign government and are operating in the United States, unless identifying those individuals could interfere with law enforcement efforts; and\n**(E)**\ngroups of people that are most vulnerable to transnational repression in the United States and, to the extent possible, in foreign countries; and\n**(2)**\na description of any actions taken by the United States Government to address transnational repression under existing law, including\u2014\n**(A)**\nsection 212(a)(3)(C) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(3)(C) );\n**(B)**\nsection 1263 of the Global Magnitsky Human Rights Accountability Act ( 22 U.S.C. 10102 );\n**(C)**\nsection 7031(c) of the Department of State, Foreign Operations, and Related Programs Appropriations Act, 2020 (division G of Public Law 116\u201394 ; 8 U.S.C. 1182 note);\n**(D)**\nprosecutions and the statutory authority authorizing such prosecutions; and\n**(E)**\nwhich agencies are conducting outreach to victims of transnational repression and the form of such outreach.\n##### (d) Form\nThe strategy required under subsection (a) shall be submitted in unclassified form, but may include a classified annex, if necessary.\n##### (e) Updates\nThe Secretary of State shall provide the congressional committee referred to in subsection (a) with annual updates regarding the implementation of such strategy.\n#### 5. Training\n##### (a) Department of State personnel\n**(1) In general**\nThe Secretary of State should make training available to Department of State personnel, including overseas mission leadership, as appropriate, and if it pertains to their countries of assignment, with respect to\u2014\n**(A)**\ntactics and practices used by perpetrators;\n**(B)**\ngovernments known to employ transnational repression;\n**(C)**\ngovernments that cooperate with other governments engaged in transnational repression;\n**(D)**\ntools of digital surveillance and other cyber tools used in transnational repression activities; and\n**(E)**\nUnited States policy priorities.\n**(2) Authorization of appropriations**\nThere is authorized to be appropriated such amounts as may be necessary for fiscal year 2026 to develop and implement the curriculum described in paragraph (1).\n##### (b) United States officials responsible for domestic threats of transnational repression\n**(1) In general**\nTo better recognize and prevent transnational repression, the Attorney General, in consultation with the Secretary of Homeland Security, the Director of National Intelligence, civil society, and the business community, shall provide training with respect to\u2014\n**(A)**\ntactics and practices used by perpetrators;\n**(B)**\ngovernments known to employ transnational repression;\n**(C)**\nwhich communities and locations in the United States are most vulnerable to transnational repression;\n**(D)**\ntools of digital surveillance and other cyber tools used in transnational repression activities; and\n**(E)**\nUnited States policy priorities.\n**(2) Training recipients**\nThose receiving the training described in paragraph (1) should be\u2014\n**(A)**\nemployees or task force members of\u2014\n**(i)**\nthe Department of Homeland Security, including U.S. Customs and Border Protection, U.S. Citizenship and Immigration Services, and U.S. Immigration and Customs Enforcement and any other employees the Secretary of Homeland Security determines should receive such training;\n**(ii)**\nthe Department of Justice, including the\u2014\n**(I)**\nFederal Bureau of Investigation; and\n**(II)**\nINTERPOL Washington; and\n**(iii)**\nthe Office of Refugee Resettlement of the Department of Health and Human Services;\n**(B)**\nother Federal, State, and local law enforcement and municipal officials receiving instruction at the Federal Law Enforcement Training Center; and\n**(C)**\nappropriate private sector and community partners of the Federal Bureau of Investigation.\n**(3) Authorization of appropriations**\nThere is authorized to be appropriated such amounts as may be necessary for fiscal year 2026 to develop and provide the curriculum and training described in paragraph (1).\n#### 6. Department of Homeland Security and Department of Justice efforts to combat transnational repression in the United States\n##### (a) In general\nThe Attorney General, in consultation with the Secretary of Homeland Security and the Director of the Federal Bureau of Investigation, shall\u2014\n**(1)**\nnot later than 270 days after the date of the enactment of this Act, publish a toolkit or guide that describes existing Federal resources to assist and protect individuals and communities targeted by transnational repression in the United States;\n**(2)**\nin cooperation with the heads of other Federal agencies, conduct proactive outreach so that individuals in targeted communities are informed about the types of criminal incidents that should be reported to the Federal Bureau of Investigation;\n**(3)**\norganize annual trainings with caseworker staff in congressional offices regarding the tactics of transnational repression and the resources available to constituents; and\n**(4)**\nproduce an assessment of how data that is purchased by governments perpetrating transnational repression is misused by\u2014\n**(A)**\nentities that are exporting dual-use spyware technology to any governments engaged in transnational repression;\n**(B)**\nentities that are buying and selling personally identifiable information that can be used to track and surveil potential victims; and\n**(C)**\nentities that are exporting items on the Commerce Control List (as set forth in Supplement No. 1 to part 774 of the Export Administration Regulations under subchapter C of chapter VII of title 15, Code of Federal Regulations) to any governments engaged in transnational repression that can be misused for human rights abuses.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated such amounts as may be necessary for fiscal year 2026 for the research, development, outreach, and training activities described in subsection (a).",
      "versionDate": "2025-08-01",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-07-29",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "2525",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Transnational Repression Policy Act",
      "type": "S"
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
        "updateDate": "2025-09-18T20:46:41Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4829ih.xml"
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
      "title": "Transnational Repression Policy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transnational Repression Policy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To address transnational repression by foreign governments against private individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:48:33Z"
    }
  ]
}
```
