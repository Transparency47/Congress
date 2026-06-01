# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8408?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8408
- Title: Legacy IT Reduction Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8408
- Origin chamber: House
- Introduced date: 2026-04-21
- Update date: 2026-04-29T20:33:54Z
- Update date including text: 2026-04-29T20:33:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-21: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-04-21: Introduced in House

## Actions

- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8408",
    "number": "8408",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000476",
        "district": "10",
        "firstName": "Maxwell",
        "fullName": "Rep. Frost, Maxwell [D-FL-10]",
        "lastName": "Frost",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Legacy IT Reduction Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-29T20:33:54Z",
    "updateDateIncludingText": "2026-04-29T20:33:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-21",
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
          "date": "2026-04-21T14:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "SC"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "MO"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8408ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8408\nIN THE HOUSE OF REPRESENTATIVES\nApril 21, 2026 Mr. Frost (for himself, Mr. Timmons , and Mr. Burlison ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require the reduction of the reliance and expenditures of the Federal Government on legacy information technology systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Legacy IT Reduction Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of General Services.\n**(2) Agency**\nThe term agency means an agency described in paragraph (1) or (2) of section 901(b) of title 31, United States Code.\n**(3) Chief information officer**\nThe term Chief Information Officer means a Chief Information Officer designated under section 3506(a)(2) of title 44, United States Code.\n**(4) Comptroller general**\nThe term Comptroller General means the Comptroller General of the United States.\n**(5) Congressional oversight committee**\nThe term congressional oversight committee means, with respect to a particular agency, a committee or subcommittee of the Senate or the House of Representatives that provides oversight of the agency.\n**(6) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(7) Information technology**\nThe term information technology has the meaning given the term in section 11101 of title 40, United States Code.\n**(8) It working capital fund; legacy information technology system**\nThe terms IT working capital fund and legacy information technology system have the meanings given the terms in section 1076 of the National Defense Authorization Act for Fiscal Year 2018 ( 40 U.S.C. 11301 note; Public Law 115\u201391 ).\n**(9) National security system**\nThe term national security system has the meaning given the term in section 11103 of title 40, United States Code.\n**(10) Technology modernization fund**\nThe term Technology Modernization Fund means the fund established under section 1078(b)(1) of the National Defense Authorization Act for Fiscal Year 2018 ( 40 U.S.C. 11301 note; Public Law 115\u201391 ).\n#### 3. Legacy information technology system inventory\n##### (a) Inventory of legacy information technology systems\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, and not later than 5 years thereafter, the Chief Information Officer of each agency shall compile an inventory that lists each legacy information technology system used, operated, or maintained by the agency.\n**(2) Contents**\nThe Director shall issue guidance prescribing the information that the Chief Information Officer of each agency shall include for each legacy technology information system listed in the inventory required under paragraph (1). In issuing such guidance, the Director shall consider including for each legacy technology information system listed in the inventory\u2014\n**(A)**\nthe name or an identification of the legacy information technology system;\n**(B)**\nthe office or mission of the agency that the legacy information technology system supports and how the office or mission uses the legacy information technology system;\n**(C)**\nwhether the legacy information technology system is connected to a non-legacy information technology system;\n**(D)**\nto the extent that information is available\u2014\n**(i)**\nthe date of the last update or refresh of the legacy information technology system;\n**(ii)**\nthe annual price, including recurring subscription costs and any costs to contract labor, to operate or maintain the legacy information technology system; and\n**(iii)**\nthe name and contact information of the vendor; and\n**(E)**\nthe date of the next expected update or modernization, retirement, or disposal of the legacy information technology system.\n##### (b) Transparency and accountability\n**(1) In general**\nUpon request by a House of Congress, a congressional oversight committee of an agency, the Comptroller General, or an inspector general of an agency, the head of the agency shall make available the inventory compiled under subsection (a)(1) or a relevant portion of that inventory.\n**(2) Reporting**\nThe Director may require an agency to include the inventory compiled under subsection (a)(1) in a reporting structure determined by the Director.\n#### 4. Agency legacy information technology systems modernization plans\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, and every 5 years thereafter, the head of an agency shall develop and include as part of the information resource management strategic plan of the agency submitted under section 3506(b)(2) of title 44, United States Code, a plan to modernize the legacy information technology systems of the agency.\n##### (b) Contents\nA modernization plan of an agency developed under subsection (a) shall include\u2014\n**(1)**\nan inventory of the legacy information technology systems of the agency;\n**(2)**\nan identification of legacy information technology systems that the agency has prioritized for updates, modernization, retirement, or disposal;\n**(3)**\nsteps the agency intends to make toward updating, modernizing, retiring, or disposing of the legacy information technology systems of the agency prioritized under paragraph (2) during the 5-year period beginning on the date of submission of the plan; and\n**(4)**\nany additional information that the Director determines necessary or useful for the agency to consider or include to effectively and efficiently execute the modernization plan, which may include\u2014\n**(A)**\nthe capacity of the agency to operate and maintain an updated or modernized legacy information technology system;\n**(B)**\nthe estimated cost and sources of funding required to execute the modernization plan;\n**(C)**\nthe ability of the agency to adapt an updated or modernized legacy information technology system to changes in policy, technology, or other user needs, as necessary; and\n**(D)**\nthe effect that updating, modernizing, retiring, or disposing of a legacy information technology system of the agency that is connected to a non-legacy information technology system would have on any such non-legacy information technology system.\n##### (c) Publication and submission to congress\nNot later than 30 days after the date on which the head of an agency submits the modernization plan developed under subsection (a) as part of the information resource management strategic plan of the agency submitted under section 3506(b)(2) of title 44, United States Code, the head of the agency shall submit the modernization plan to the Committee on Homeland Security and Governmental Affairs of the Senate, the Committee on Oversight and Accountability of the House of Representatives, and each congressional oversight committee of the agency.\n#### 5. Role of the office of management and budget\nNot later than 180 days after the date of enactment of this Act, the Director, in coordination with the Administrator of the Office of Electronic Government, shall issue guidance on the implementation of this Act, which shall include\u2014\n**(1)**\ncriteria to determine whether information technology qualifies as a legacy information technology system for the purposes of compiling the inventory required under section 3(a)(1);\n**(2)**\ninstructions and templates to inform the compilation of the inventory required under section 3(a)(1), as necessary;\n**(3)**\ninstructions and templates to inform the compilation and publication of, and any subsequent updates to, the modernization plans required under section 4(a), as necessary; and\n**(4)**\nany other guidance determined necessary for the implementation of this Act, including how the implementation of this Act complements laws, regulations, and guidance relating to information technology modernization.\n#### 6. Comptroller general review\n##### (a) In general\nNot later than 3 years after the date of enactment of this Act, the Comptroller General shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Accountability of the House of Representatives a report on\u2014\n**(1)**\nthe implementation of this Act; and\n**(2)**\nhow this Act functions alongside other information technology modernization offices, policies, and programs, such as\u2014\n**(A)**\nthe Technology Modernization Fund and the IT working capital fund;\n**(B)**\nthe Federal Risk and Authorization Management Program, the 18F program, and the 10X program of the General Services Administration;\n**(C)**\nprograms and policies of the Office of Management and Budget, including the Office of Electronic Government and the United States Digital Service; and\n**(D)**\nany other office, policy, or program of the Federal Government determined relevant by the Comptroller General.\n#### 7. Protection of sensitive information; exemption of national security systems\n##### (a) In general\nNothing in this Act shall be construed to require the head of an agency to disclose sensitive information that\u2014\n**(1)**\nis protected from disclosure under any other law; or\n**(2)**\nwould compromise the security of any information technology system of the Federal Government.\n##### (b) Exemption\nNothing in this Act shall be construed to authorize or require the head of an agency to inventory, develop a report relating to, or transfer a national security system.\n##### (c) Rule of construction\nNothing in this Act shall be construed to authorize the transfer of legacy information technology systems or equipment to the Chinese Communist Party, the People\u2019s Republic of China, or any entity controlled by the People\u2019s Republic of China.\n#### 8. No new funds; sunset\n##### (a) No new funds\nNo additional funds are authorized to be appropriated to carry out this Act.\n##### (b) Sunset\nEffective on the date that is 6 years after the date of enactment of the Act, this Act shall have no force or effect.",
      "versionDate": "2026-04-21",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-29T20:33:54Z"
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
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8408ih.xml"
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
      "title": "Legacy IT Reduction Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T06:08:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Legacy IT Reduction Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-28T06:08:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the reduction of the reliance and expenditures of the Federal Government on legacy information technology systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-28T06:03:31Z"
    }
  ]
}
```
