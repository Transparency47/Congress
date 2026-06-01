# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2427?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2427
- Title: Stop Disaster Price Gouging Act
- Congress: 119
- Bill type: HR
- Bill number: 2427
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2025-05-21T18:09:02Z
- Update date including text: 2025-05-21T18:09:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2427",
    "number": "2427",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "F000483",
        "district": "30",
        "firstName": "Laura",
        "fullName": "Rep. Friedman, Laura [D-CA-30]",
        "lastName": "Friedman",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Stop Disaster Price Gouging Act",
    "type": "HR",
    "updateDate": "2025-05-21T18:09:02Z",
    "updateDateIncludingText": "2025-05-21T18:09:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2427ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2427\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Ms. Friedman (for herself and Mr. Sherman ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit price gouging as an unfair and deceptive act or practice during a major disaster or emergency, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Disaster Price Gouging Act .\n#### 2. Prohibition on price gouging\n##### (a) Prohibition\n**(1) In general**\nExcept as provided in paragraph (2), during the period described below after the date on which the President declares a major disaster or emergency under section 401 or 501 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ; 5191) and within the area in which the disaster or emergency is declared a person\u2014\n**(A)**\nmay not increase the price as of the day before such date by more than 10 percent\u2014\n**(i)**\nwith respect to essential consumer goods and services, hotel lodging, and residential rental properties, for a period of 30 days; and\n**(ii)**\nwith respect to repair or reconstruction services, for a period of 180 days; and\n**(B)**\nmay not charge a price for essential consumer goods and services, hotel lodging, residential rental property, or reconstruction services that is more than 50 percent greater than the cost to the person for 30 days after such date if the person did not charge that price before such date.\n**(2) Exception**\nThe prohibition described in paragraph (1) does not apply as follows:\n**(A)**\nIf the increased price\u2014\n**(i)**\nis\u2014\n**(I)**\ndirectly attributable to additional cost paid by the person to a supplier of the goods or for labor or materials used to provide services; and\n**(II)**\nis not more than 10 percent greater than the total of the cost to the person plus the markup customarily applied by that seller for that good or service in the usual course of business immediately prior to the onset of the major disaster or emergency; or\n**(ii)**\nis directly attributable to tariffs or national trade policies.\n**(B)**\nFor a hotel or motel rate, if the increased price is attributable to seasonable adjustments that are regularly scheduled.\n**(C)**\nFor a rental rate, if the increased price is directly attributable to additional costs for repairs or additions beyond normal maintenance that were amortized over the rental term that caused the rent to be increased greater than 10 percent or that an increase was contractually agreed to by the tenant prior to the disaster or emergency.\n##### (b) Enforcement by Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of subsection (a) or a regulation promulgated under such subsection shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of Commission**\nThe Federal Trade Commission shall enforce subsection (a) and any regulation promulgated under such subsection in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act. Any person who violates such subsection or a regulation promulgated under such subsection shall be subject to the penalties described in subsection (e) and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n##### (c) Actions by States\n**(1) In general**\nIn any case in which the attorney general of a State, or an official or agency of a State, has reason to believe that an interest of the residents of such State has been or is threatened or adversely affected by an act or practice in violation of subsection (a) or a regulation promulgated under such subsection, the State, as parens patriae, may bring a civil action on behalf of the residents of the State in an appropriate State court or an appropriate district court of the United States to\u2014\n**(A)**\nenjoin such act or practice;\n**(B)**\nenforce compliance with such subsection or such regulation;\n**(C)**\nobtain damages, restitution, or other compensation on behalf of residents of the State; or\n**(D)**\nobtain such other legal and equitable relief as the court may consider to be appropriate.\n**(2) Notice**\nBefore filing an action under this subsection, the attorney general, official, or agency of the State involved shall provide to the Commission a written notice of such action and a copy of the complaint for such action. If the attorney general, official, or agency determines that it is not feasible to provide the notice described in this paragraph before the filing of the action, the attorney general, official, or agency shall provide written notice of the action and a copy of the complaint to the Commission immediately upon the filing of the action.\n**(3) Authority of Federal Trade Commission**\n**(A) In general**\nOn receiving notice under paragraph (2) of an action under this subsection, the Commission shall have the right\u2014\n**(i)**\nto intervene in the action;\n**(ii)**\nupon so intervening, to be heard on all matters arising therein; and\n**(iii)**\nto file petitions for appeal.\n**(B) Limitation on State action while Federal action is pending**\nIf the Commission or the Attorney General of the United States has instituted a civil action for violation of subsection (a) or a regulation promulgated under such subsection (referred to in this subparagraph as the Federal action ), no State attorney general, official, or agency may bring an action under this subsection during the pendency of the Federal action against any defendant named in the complaint in the Federal action for any violation of such subsection or regulation alleged in such complaint.\n**(4) Rule of construction**\nFor purposes of bringing a civil action under this subsection, nothing in this Act shall be construed to prevent an attorney general, official, or agency of a State from exercising the powers conferred on the attorney general, official, or agency by the laws of such State to conduct investigations, administer oaths and affirmations, or compel the attendance of witnesses or the production of documentary and other evidence.\n##### (d) Private right of action\n**(1) In general**\nA person injured by an act or practice in violation of subsection (a) or a regulation promulgated under such subsection may bring in an appropriate State court or an appropriate district court of the United States\u2014\n**(A)**\nan action to enjoin the violation;\n**(B)**\nan action to recover damages for actual monetary loss from the violation; or\n**(C)**\nboth such actions.\n**(2) Willful violations**\nIf the court finds that the defendant acted willfully in committing a violation described in paragraph (1), the court may, in its discretion, increase the amount of the award to an amount equal to not more than 3 times the amount available under paragraph (1)(B).\n**(3) Costs and attorney\u2019s fees**\nThe court shall award to a prevailing plaintiff in an action under this subsection the costs of such action and reasonable attorney\u2019s fees, as determined by the court.\n**(4) Limitation**\nAn action may be commenced under this subsection not later than 2 years after the date on which the person first discovered or had a reasonable opportunity to discover the violation.\n**(5) Nonexclusive remedy**\nThe remedy provided by this subsection shall be in addition to any other remedies available to the person.\n##### (e) Amount of civil penalties\n**(1) In general**\nFor purposes of the penalties described in subsection (b), the amount determined under this paragraph is the amount calculated by multiplying the number of violations of subsection (a) by an amount not greater than $25,000. Each violation shall be treated as a separate violation.\n**(2) Maximum total liability**\nNotwithstanding the number of actions which may be brought against a person under subsection (b), the total amount of civil penalties assessed against such person for all violations of subsection (a) and the regulations promulgated under such subsection resulting from the same or related acts or practices may not exceed $25,000.\n**(3) Adjustment for inflation**\nBeginning on the date that the Consumer Price Index is first published by the Bureau of Labor Statistics that is at least 1 year after the date of the enactment of this Act, and each year thereafter, the amount specified in paragraphs (1) and (2) shall be increased by the percentage increase, if any, in the Consumer Price Index published on such date from the Consumer Price Index published the previous year.\n**(4) Funding for disaster zones**\nAny amount recovered under subsection (b) shall be deposited into a fund to assist communities located in an area affected by a major disaster or emergency declared by the President under section 401 or 501 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ; 5191).\n##### (f) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Essential consumer goods and services**\nThe term essential consumer goods and services means goods and services that are necessary for survival and recovery during and after a major disaster or emergency and include any of the following:\n**(A)**\nFood and drink, including food and drink for animals.\n**(B)**\nEmergency supplies such as water, generators, flashlights, radios, batteries, candles, blankets, soap, diapers, temporary shelters, tape, toiletries, plywood, nails, and hammers.\n**(C)**\nMedical supplies such as prescription and non prescription medications, bandages, gauze, isopropyl alcohol, and antibacterial products.\n**(D)**\nHome heating oil.\n**(E)**\nBuilding and construction materials such as lumber, construction tools, and windows.\n**(F)**\nTransportation.\n**(G)**\nFreight.\n**(H)**\nStorage services.\n**(I)**\nGasoline and other motor fuels.\n##### (g) Relation to State law\nNothing in this Act may be construed to preempt any provision of State law that does not conflict with this Act.",
      "versionDate": "2025-03-27",
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
        "name": "Emergency Management",
        "updateDate": "2025-05-21T18:09:02Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2427ih.xml"
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
      "title": "Stop Disaster Price Gouging Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-29T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Disaster Price Gouging Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-29T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit price gouging as an unfair and deceptive act or practice during a major disaster or emergency, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-29T04:18:26Z"
    }
  ]
}
```
