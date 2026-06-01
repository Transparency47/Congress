# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3821?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3821
- Title: Fair Repair Act
- Congress: 119
- Bill type: S
- Bill number: 3821
- Origin chamber: Senate
- Introduced date: 2026-02-10
- Update date: 2026-04-29T19:27:53Z
- Update date including text: 2026-04-29T19:27:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in Senate
- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-02-10: Introduced in Senate

## Actions

- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3821",
    "number": "3821",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Fair Repair Act",
    "type": "S",
    "updateDate": "2026-04-29T19:27:53Z",
    "updateDateIncludingText": "2026-04-29T19:27:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T20:33:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3821is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3821\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2026 Mr. Luj\u00e1n introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require original equipment manufacturers of digital electronic equipment to make available certain documentation, diagnostic, and repair information to independent repair providers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Repair Act .\n#### 2. Requirements for original equipment manufacturers\n##### (a) In general\nIn the case of digital electronic equipment manufactured by or on behalf of, sold, or otherwise supplied by an original equipment manufacturer, the original equipment manufacturer shall make available, for the purposes of diagnosis, maintenance, or repair of such equipment, to independent repair providers and owners of such equipment on fair and reasonable terms, documentation, parts, and tools, inclusive of any updates.\n##### (b) Prohibition on the use of certain parts\nAn original equipment manufacturer shall not use parts pairing or any other mechanism to\u2014\n**(1)**\nprevent the installation or functioning of any otherwise-functional part, including a non-manufacturer approved replacement part or component;\n**(2)**\ninhibit or reduce the functioning of any part, such that replacement by an independent repair provider or the equipment owner would cause the equipment to operate with reduced functionality or performance;\n**(3)**\ncreate false, misleading, deceptive, or non-dismissible alerts or warnings about parts;\n**(4)**\ncharge additional fees or increased prices for future repairs; or\n**(5)**\nlimit who can purchase parts or perform repair services.\n#### 3. Enforcement\n##### (a) Enforcement by the Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of section 2 shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Commission shall enforce this Act and any regulations promulgated under this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act, and any person who violates this Act or a regulation promulgated under this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(B) Regulations**\nThe Commission may, under section 553 of title 5, United States Code, prescribe any regulations it determines necessary to carry out this Act.\n**(C) Effect on other laws**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n##### (b) Enforcement by State attorneys general\n**(1) In general**\nIf the chief law enforcement officer of a State, or an official or agency designated by a State, has reason to believe that any person has violated or is violating section 2, the attorney general, official, or agency of the State, in addition to any authority it may have to bring an action in State court under State law, may bring a civil action in any appropriate United States district court or in any other court of competent jurisdiction, including a State court, to\u2014\n**(A)**\nenjoin further such violation by such person;\n**(B)**\nenforce compliance with such section;\n**(C)**\nobtain civil penalties; and\n**(D)**\nobtain damages, restitution, or other compensation on behalf of residents of the State.\n**(2) Notice and intervention by the FTC**\nThe attorney general (or other such officer) of a State shall provide prior written notice of any action under paragraph (1) to the Commission and provide the Commission with a copy of the complaint in the action, except in any case in which such prior notice is not feasible, in which case the attorney general shall serve such notice immediately upon instituting such action. The Commission shall have the right\u2014\n**(A)**\nto intervene in the action;\n**(B)**\nupon so intervening, to be heard on all matters arising therein; and\n**(C)**\nto file petitions for appeal.\n**(3) Limitation on State action while Federal action is pending**\nIf the Commission has instituted a civil action for violation of this Act, no State attorney general, or official or agency of a State, may bring an action under this paragraph during the pendency of that action against any defendant named in the complaint of the Commission for any violation of this Act alleged in the complaint.\n**(4) Relationship with State law claims**\nIf the attorney general of a State has authority to bring an action under State law directed at acts or practices that also violate this Act, the attorney general may assert the State law claim and a claim under this Act in the same civil action.\n#### 4. Rules of construction, limitations, and non-application\nThe following rules of construction, limitations, and non-application provisions apply to this Act:\n**(1) Security-related functions not excluded**\nFor digital electronic equipment that contains an electronic security lock or other security-related function, the original equipment manufacturer shall make available to the owner and to independent repair providers, on fair and reasonable terms, any special documentation, tools, and parts needed to disable the lock or function, and to reset it when disabled in the course of diagnosis, maintenance, or repair of the equipment, to restore full functionality of the equipment.\n**(2) Protection of trade secrets**\nNothing in this Act shall be construed to require an original equipment manufacturer to divulge a trade secret, as defined in section 1839 of title 18, United States Code, to an owner or an independent repair provider except as necessary to provide documentation, parts, and tools on fair and reasonable terms.\n**(3) Terms of agreement with authorized repair providers**\nNo provision in this Act shall be construed to abrogate, interfere with, contradict, or alter the terms of any arrangement described in section 6(1)(A), including the performance or provision of warranty or recall repair work by an authorized repair provider on behalf of an original equipment manufacturer pursuant to such arrangement, except that any provision in such terms that purports to waive, avoid, restrict, or limit an OEM's obligations to comply with this Act shall be void and unenforceable.\n**(4) Non-application to motor vehicle or motor vehicle equipment manufacturers**\nNothing in this Act shall apply to a motor vehicle manufacturer, a manufacturer of motor vehicle equipment, or a motor vehicle dealer, acting in that capacity.\n**(5) Non-application to manufacturers of medical devices**\nNothing in this Act shall apply to a manufacturer of a medical device, acting in that capacity.\n**(6) Non-application to manufacturers of off-road or non-road vehicles**\nNothing in this Act shall apply to any manufacturer, distributor, importer, or dealer of an off-road or non-road vehicle, acting in that capacity, including without limitation, aircraft, motorcycles, marine vessels, all terrain sports vehicles, utility terrain vehicles, recreational vehicles, and racing vehicles.\n**(7) Non-application to manufacturers of safety communications equipment**\nNothing in this Act shall apply to any manufacturer of safety communications equipment, the intended use of which is for emergency response or prevention purposes by an emergency services organization, such as police, fire, or medical and emergency rescue services agencies, acting in that capacity.\n#### 5. Limitation of liability\n##### (a) Damage resulting from repair\nNo original equipment manufacturer or authorized repair provider shall be liable for any damage or injury to any digital electronic equipment, person, or property that occurs as a result of repair, diagnosis, maintenance, or modification performed by an independent repair provider or owner, or any other use by an independent repair provider or owner of parts, tools, or documentation provided by an original equipment manufacturer, including with respect to any\u2014\n**(1)**\nindirect, incidental, special, or consequential damages;\n**(2)**\nloss of data, privacy, or profits; or\n**(3)**\ninability to use, or reduced functionality of, the digital electronic equipment.\n##### (b) No warranty for independent repair providers or owners\nAn original equipment manufacturer shall not be required to warrant any repairs provided by independent repair providers or owners.\n##### (c) Improper use of personal data\nNo original equipment manufacturer shall be liable for improper use of personal data or any data privacy or security breach in connection with repair, diagnosis, maintenance, or modification performed by an independent repair provider or owner.\n#### 6. Definitions\nIn this Act, the following definitions apply:\n**(1) Authorized repair provider**\n**(A) In general**\nThe term authorized repair provider means with respect to an OEM, a person that\u2014\n**(i)**\nhas an arrangement with the OEM in which the OEM grants to the person license to use a trade name, service mark, or other proprietary identifier for the purposes of offering the services of diagnosis, maintenance, or repair of digital electronic equipment under the name of the OEM; or\n**(ii)**\notherwise has an arrangement with the OEM to offer such services on behalf of or under contract with the OEM.\n**(B) Clarification**\nAn OEM that offers the services of diagnosis, maintenance, or repair of digital electronic equipment manufactured by it or on its behalf, or sold or otherwise supplied by the OEM, shall be considered an authorized repair provider with respect to such equipment.\n**(2) Digital electronic equipment**\nThe term digital electronic equipment means any product that depends for its functioning, in whole or in part, on digital electronics embedded in or attached to the product.\n**(3) Documentation**\nThe term documentation means any manuals, diagrams, reporting output, service code descriptions, schematic, security code or password, or other information used in effecting the services of diagnosis, maintenance, or repair of digital electronic equipment.\n**(4) Fair and reasonable terms**\nThe term fair and reasonable terms , with respect to a part, tool, or documentation, means at costs and terms that are equivalent to the most favorable costs and terms under which an OEM offers the part, tool, or documentation to an authorized repair provider\u2014\n**(A)**\naccounting for any discount, rebate, convenient and timely means of delivery, means of enabling fully restored and updated functionality, rights of use, or other incentive or preference the OEM offers to an authorized repair provider, and for any additional cost, burden, or impediment the OEM imposes on an owner or independent repair provider;\n**(B)**\nnot conditioned on or imposing a substantial obligation or restriction that is not reasonably necessary for enabling the owner or independent repair provider to engage in the diagnosis, maintenance, or repair of digital electronic equipment made by or on behalf of the OEM; and\n**(C)**\nnot conditioned on an arrangement described in paragraph (1)(A).\n**(5) Independent repair provider**\n**(A) In general**\nThe term independent repair provider means with respect to an OEM, a person that is not affiliated with the OEM or with an authorized repair provider of the OEM, when such person is engaged in the diagnosis, maintenance, or repair of digital electronic equipment manufactured by or on behalf of, sold, or otherwise supplied by the OEM.\n**(B) Clarification**\nAn OEM or, with respect to that OEM, a person who has an arrangement described in paragraph (1)(A) with that OEM, or who is affiliated with a person who has such an arrangement with that OEM, shall be considered an independent repair provider for the purposes of those instances when such OEM or person engages in the diagnosis, service, maintenance, or repair of digital equipment that is not manufactured by or on behalf of, sold, or otherwise supplied by that OEM.\n**(6) Medical device**\nThe term medical device has the meaning given the term device under section 201(h) of the Federal Food, Drug and Cosmetic Act ( 21 U.S.C. 321(h) ).\n**(7) Motor vehicle**\nThe term motor vehicle means a vehicle that is designed for transporting persons or property on a street or highway and is certified by the manufacturer under all applicable Federal safety and emissions standards and requirements for distribution and sale in the United States.\n**(8) Motor vehicle dealer**\nThe term motor vehicle dealer means a person who\u2014\n**(A)**\nis engaged in the business of selling or leasing new motor vehicles to another person pursuant to a franchise agreement;\n**(B)**\nhas obtained a license to engage in such business under the applicable State law; and\n**(C)**\nis engaged in the services of diagnosis, maintenance, or repair of motor vehicles or motor vehicle engines pursuant to such franchise agreement.\n**(9) Motor vehicle manufacturer**\nThe term motor vehicle manufacturer means a person engaged in the business of manufacturing or assembling new motor vehicles.\n**(10) Original equipment manufacturer; OEM**\nThe term original equipment manufacturer or OEM means a person who is engaged in the business of selling, leasing, or otherwise supplying new digital electronic equipment or parts of equipment manufactured by or on behalf of itself, to any person.\n**(11) Owner**\nThe term owner means a person who owns or leases digital electronic equipment.\n**(12) Part**\nThe term part means any replacement part, either new or used, made available by or to an OEM for purposes of effecting the services of maintenance or repair of digital electronic equipment manufactured by or on behalf of, sold, or otherwise supplied by the OEM.\n**(13) Parts pairing**\nThe term parts pairing means, with respect to a part, the practice of employing software to identify component parts through the use of a unique identifier.\n**(14) Tool**\nThe term tool means any software program, hardware implement, or other apparatus used for diagnosis, maintenance, or repair of digital electronic equipment, including software or other mechanisms that provision, program, or pair a part, calibrate functionality, or perform any other function required to bring the equipment back to fully functional condition.\n#### 7. Effective date\nThis Act shall take effect 60 days after the date of enactment of this Act and shall apply with respect to equipment sold or in use on or after the effective date of this Act.",
      "versionDate": "2026-02-10",
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
        "actionDate": "2026-02-05",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "7404",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fair Repair Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2026-02-27T16:36:01Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3821is.xml"
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
      "title": "Fair Repair Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair Repair Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require original equipment manufacturers of digital electronic equipment to make available certain documentation, diagnostic, and repair information to independent repair providers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T04:48:25Z"
    }
  ]
}
```
