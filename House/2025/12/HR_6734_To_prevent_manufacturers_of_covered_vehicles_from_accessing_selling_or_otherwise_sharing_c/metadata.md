# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6734?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6734
- Title: Auto Data Privacy and Autonomy Act
- Congress: 119
- Bill type: HR
- Bill number: 6734
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-04-29T12:55:12Z
- Update date including text: 2026-04-29T12:55:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6734",
    "number": "6734",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B001316",
        "district": "7",
        "firstName": "Eric",
        "fullName": "Rep. Burlison, Eric [R-MO-7]",
        "lastName": "Burlison",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Auto Data Privacy and Autonomy Act",
    "type": "HR",
    "updateDate": "2026-04-29T12:55:12Z",
    "updateDateIncludingText": "2026-04-29T12:55:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T15:03:40Z",
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
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "MO"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "AZ"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "TN"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6734ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6734\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mr. Burlison introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prevent manufacturers of covered vehicles from accessing, selling, or otherwise sharing covered data without consent of covered vehicle owners, to require manufacturers of covered vehicles to provide covered vehicle owners with access to, and control of, covered data, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Auto Data Privacy and Autonomy Act .\n#### 2. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Covered data**\nThe term covered data means user data and vehicle-generated data.\n**(3) Covered vehicle**\nThe term covered vehicle means a motor vehicle or a vehicle primarily used for farming or construction.\n**(4) Geolocation data**\nThe term geolocation data means information that reveals the past or present physical location of an individual, a covered vehicle, or device.\n**(5) Motor vehicle**\nThe term motor vehicle has the same meaning given such term in section 30102(a) of title 49, United States Code, and includes a motor vehicle trailer.\n**(6) Personally identifiable information**\nThe term personally identifiable information means information that\u2014\n**(A)**\ndirectly identifies an individual such as the name, address, social security number or other identifying number or code, telephone number, or email address of an individual;\n**(B)**\nindirectly identifies an individual such as the gender, race, or date of birth of an individual; or\n**(C)**\nreveals the geolocation data or internet activity of an individual.\n**(7) User data**\nThe term user data means data transferred to a covered vehicle by the owner or user of such vehicle.\n**(8) User preference**\nThe term user preference means any choice with respect to a configurable setting of a covered vehicle made by or for the benefit of the owner or user of such covered vehicle.\n**(9) Vehicle-generated data**\nThe term vehicle-generated data means all electronic data generated or processed onboard a covered vehicle, such as data generated by sensors, receivers, computer processing units, or other vehicle components and includes the geolocation data of such covered vehicle.\n#### 3. User data and vehicle-generated data privacy and security\n##### (a) Prohibition on manufacturers\nWith respect to a covered vehicle, a manufacturer of such vehicle may not\u2014\n**(1)**\naccess covered data, unless\u2014\n**(A)**\nthe owner of such covered vehicle or, in the event of the death or incapacity of such owner, the next of kin of such owner affirmatively consents to such manufacturer accessing such data and such consent\u2014\n**(i)**\nis freely given;\n**(ii)**\nis informed, specific, and unambiguous;\n**(iii)**\nis in writing; and\n**(iv)**\nmay be easily withdrawn; or\n**(B)**\nsuch data is accessed solely to improve covered vehicle performance or safety;\n**(2)**\nsell, lease, or otherwise share covered data, unless\u2014\n**(A)**\nrequired to do so\u2014\n**(i)**\npursuant to a lawfully executed warrant;\n**(ii)**\npursuant to a court order that provides the covered vehicle owner notice of the order and at least 48 hours to object and request a hearing; or\n**(iii)**\nto facilitate an emergency response; or\n**(B)**\nthe owner of such covered vehicle, or, in the event of the death or incapacity of such owner, the next of kin of such owner, affirmatively consents to such manufacturer to do so and such consent\u2014\n**(i)**\nis freely given;\n**(ii)**\nis informed, specific, and unambiguous;\n**(iii)**\nis in writing; and\n**(iv)**\nmay be easily withdrawn; or\n**(3)**\nsell, license, rent, trade, transfer, release, disclose, provide access to, or otherwise make available personally identifiable information of a United States citizen or lawful permanent resident to the following:\n**(A)**\nThe Democratic People\u2019s Republic of Korea.\n**(B)**\nThe People\u2019s Republic of China.\n**(C)**\nThe Russian Federation.\n**(D)**\nThe Islamic Republic of Iran.\n**(E)**\nThe Bolivarian Republic of Venezuela.\n##### (b) Report\nNot later than 180 days after the date of the enactment of this Act, the Commission shall, in consultation with the Attorney General, the Secretary of Homeland Security, the Secretary of Transportation, and the Federal Communications Commission, submit to Congress a report that describes with respect to covered data\u2014\n**(1)**\nthe types of such data that a manufacturer of a covered vehicle accesses;\n**(2)**\nthe individuals and entities, other than a manufacturer of a covered vehicle, that access such data;\n**(3)**\nthe Federal or State Government entities that access such data and how such entities use such data;\n**(4)**\nthe individuals and entities to whom such data may be sold or otherwise shared;\n**(5)**\nthe foreign governments to whom such data may be sold or otherwise shared and how such data is used by such foreign governments;\n**(6)**\nthe cybersecurity capabilities and risks associated with covered vehicles;\n**(7)**\noccurrences of such data being compromised, including the prevalence of such occurrences and any entities with ties to foreign governments associated with such occurrences; and\n**(8)**\na description of the feasibility of a technology-neutral, standards-based, secure interface to allow an owner of a covered vehicle access to such data designed without preference or prejudice towards any technology or service used to access and control such data by such owner, and not contingent on ownership or licensing of proprietary technologies by such owner or a manufacturer of a covered vehicle.\n#### 4. Vehicle owner\u2019s data access and control\n##### (a) In general\nThe manufacturer of a covered vehicle shall provide to an owner of such vehicle access to, and control of, all covered data generated or processed onboard, or transferred to, such vehicle\u2014\n**(1)**\nat no cost beyond the purchase price of such vehicle;\n**(2)**\nin real time;\n**(3)**\nwithout any restriction or limitation on use or authorizing access to third parties;\n**(4)**\nwithout a requirement that the covered vehicle owner pay a fee or purchase a license to decrypt such data or use a device provided by such manufacturer to access and use such data;\n**(5)**\nthrough the vehicle\u2019s interface port and through wireless transmission of such data to the extent such vehicle is equipped with technology to wirelessly transmit such data; and\n**(6)**\nin a manner that enables the operation of an open application programming interface that\u2014\n**(A)**\nfacilitates deletion of all user data stored in a covered vehicle; and\n**(B)**\nenables the setting of any user preference by the covered vehicle owner or another user of the covered vehicle.\n##### (b) Relation to other laws\nThis section supersedes any statute, rule, requirement or other legal obligation of a State of political subdivision thereof that relates to the requirements of this section.\n#### 5. Enforcement\n##### (a) Unfair or deceptive act or practice\nA violation of this Act shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n##### (b) Powers of the Commission\n**(1) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(2) Privileges and immunities**\nAny person who violates this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n#### 6. Disclosure of confidential business information\nExcept as provided in section 4, nothing in this Act shall require a manufacturer of a covered vehicle to divulge confidential business information (as that term is defined in section 512.3(c) of title 49, Code of Federal Regulations).\n#### 7. Effective date\nThis Act shall take effect on the date that is 3 months after the date of enactment of this Act.\n#### 8. No new appropriations\nNo additional funds are authorized to be appropriated to carry out this Act. The Commission shall carry out this Act using amounts otherwise appropriated.",
      "versionDate": "2025-12-16",
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
        "actionDate": "2025-12-16",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "3494",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Auto Data Privacy and Autonomy Act",
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
        "name": "Commerce",
        "updateDate": "2026-01-09T16:23:42Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6734ih.xml"
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
      "title": "Auto Data Privacy and Autonomy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-08T06:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Auto Data Privacy and Autonomy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-08T06:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prevent manufacturers of covered vehicles from accessing, selling, or otherwise sharing covered data without consent of covered vehicle owners, to require manufacturers of covered vehicles to provide covered vehicle owners with access to, and control of, covered data, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-08T06:03:21Z"
    }
  ]
}
```
