# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6687?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6687
- Title: DRIVER Act
- Congress: 119
- Bill type: HR
- Bill number: 6687
- Origin chamber: House
- Introduced date: 2025-12-12
- Update date: 2026-02-21T09:05:43Z
- Update date including text: 2026-02-21T09:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-12: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-12: Introduced in House

## Actions

- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-12",
    "latestAction": {
      "actionDate": "2025-12-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6687",
    "number": "6687",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "H001086",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
        "lastName": "Harshbarger",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "DRIVER Act",
    "type": "HR",
    "updateDate": "2026-02-21T09:05:43Z",
    "updateDateIncludingText": "2026-02-21T09:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
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
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-12",
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
          "date": "2025-12-12T14:00:30Z",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "TX"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "PA"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "MO"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6687ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6687\nIN THE HOUSE OF REPRESENTATIVES\nDecember 12, 2025 Mrs. Harshbarger (for herself, Mr. Weber of Texas , and Mr. Perry ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require manufacturers of motor vehicles to provide motor vehicle owners with access to and use of motor vehicle data of motor vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Data Rights for Information and Vehicle Electronics in Real-time Act or the DRIVER Act .\n#### 2. Motor vehicle owner access to motor vehicle data\nA manufacturer of a motor vehicle shall provide to a motor vehicle owner secure access to, and joint control of, any motor vehicle data of the motor vehicle of such motor vehicle owner as follows:\n**(1)**\nAt no cost beyond the purchase price of such motor vehicle.\n**(2)**\nIn real time.\n**(3)**\nWithout any restriction or limitation with respect to the manner in which such motor vehicle owner, for any lawful purpose\u2014\n**(A)**\nuses such motor vehicle data; or\n**(B)**\nauthorizes access to or use of such motor vehicle data by a third party, other than a person owned or controlled by a foreign adversary (as defined in section 791.2 of title 15, Code of Federal Regulations).\n**(4)**\nWithout a requirement that such motor vehicle owner pay a fee or purchase a license to decrypt such motor vehicle data or use a device provided by such manufacturer to access and use such motor vehicle data.\n**(5)**\nThrough a motor vehicle interface port (such as an on-board diagnostics port) of such motor vehicle and through wireless transmission of such motor vehicle data (to the extent such motor vehicle is equipped with technology to wirelessly transmit such motor vehicle data).\n**(6)**\nIn a manner that facilitates the deletion of any user data stored in such motor vehicle.\n**(7)**\nIn compliance with any voluntary automotive industry cybersecurity standards requirements (such as ISO/SAE 24134).\n#### 3. Additional motor vehicle owner data access controls\n##### (a) Vehicle owners\u2019 data access control with respect to motor vehicle manufacturers\nA manufacturer of a motor vehicle may not, with respect to a motor vehicle manufactured by such manufacturer, sell any covered data unless the manufacturer provides to the motor vehicle owner of such motor vehicle a clear and conspicuous opportunity to opt out of any such sale.\n##### (b) Fleet vehicle drivers\u2019 data access control with respect to motor vehicle fleet owners\n**(1) In general**\nA motor vehicle fleet owner may not, with respect to a motor vehicle that such motor vehicle fleet owner leases or in which such motor vehicle fleet owner has an ownership or contracted beneficial interest, sell any covered data, unless the motor vehicle fleet owner provides to the driver or operator of such motor vehicle a clear and conspicuous opportunity to opt out of any such sale.\n**(2) Limitation**\nThe requirement to provide an opportunity to opt out described in paragraph (1) does not apply if the relevant data is generated by a commercial or governmental fleet vehicle driven by a driver in the course of the employment of the driver, except if such driver behavior data is to be sold for the purpose of profiling in furtherance of decisions that knowingly cause negative legal or similarly significant harmful effects concerning the conduct of a person outside the course of the employment of the person.\n##### (c) National security\nA manufacturer of a motor vehicle or a motor vehicle fleet owner may not knowingly sell motor vehicle data to any of the following:\n**(1)**\nThe Democratic People\u2019s Republic of Korea.\n**(2)**\nThe People\u2019s Republic of China.\n**(3)**\nThe Russian Federation.\n**(4)**\nThe Islamic Republic of Iran.\n**(5)**\nThe Bolivarian Republic of Venezuela.\n##### (d) Exceptions\nFor purposes of this section, a sale does not include any of the following activities:\n**(1)**\nTransferring covered data to emergency responders.\n**(2)**\nResponding to an owner-initiated communication originating from within a motor vehicle or an app, where covered data may be transferred only to provide the response.\n**(3)**\nResponding to a vehicle-initiated communication related to the safe operation of a motor vehicle, where covered data may be transferred only to provide the response.\n**(4)**\nResponding to a driver or user-initiated communication originating from within a motor vehicle or an app, where covered data may be transferred only to provide the response.\n**(5)**\nConducting research or efforts to improve, repair, enhance the safety of, or develop products, services, or technology.\n**(6)**\nInvestigating or defending claims and losses.\n**(7)**\nConducting investigations of potential product quality, fraud, theft, or safety issues.\n**(8)**\nDetermining or effectuating vehicle field actions, including customer satisfaction campaigns, technical service bulletins, compliance recalls, and safety recalls.\n**(9)**\nDetecting or responding to cybersecurity incidents.\n**(10)**\nAdministering and fulfilling motor vehicle warranties.\n**(11)**\nPerforming diagnostics and prognostics of a motor vehicle or a component of a motor vehicle.\n**(12)**\nIdentifying and addressing issues that impair functionality.\n**(13)**\nDisclosing covered data to a processor that processes such covered data on behalf of a manufacturer of a motor vehicle or a motor vehicle fleet owner.\n**(14)**\nDisclosing or transferring covered data to an affiliate of a manufacturer of a motor vehicle or a motor vehicle fleet owner.\n**(15)**\nDisclosing information that a consumer\u2014\n**(A)**\nintentionally makes available to the general public through a channel of mass media; and\n**(B)**\ndoes not restrict to a specific audience.\n**(16)**\nDisclosing or transferring covered data to a third party as an asset that is part of a proposed or an actual merger, acquisition, bankruptcy, or other transaction in which the third party assumes control of all or part of the assets of a controller.\n**(17)**\nComplying with a lawfully executed warrant.\n**(18)**\nComplying with a court order.\n#### 4. Enforcement by Commission\n##### (a) Unfair or deceptive acts or practices\nA violation of section 2 shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n##### (b) Powers of Commission\nThe Commission shall enforce section 2 in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act, and any person who violates such section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n#### 5. Disclosure of confidential business information\nExcept as provided in section 2, nothing in this Act shall be construed to require a motor vehicle manufacturer to divulge confidential business information (as defined in section 512.3(c) of title 49, Code of Federal Regulations).\n#### 6. Relationship to State law\nNo State, or political subdivision of a State, may maintain, enforce, prescribe, or continue in effect any law, rule, regulation, requirement, standard, or other provision having the force and effect of law that relates to section 2 of this Act.\n#### 7. Definitions\nIn this Act:\n**(1) Biometric identifier**\nThe term biometric identifier means motor vehicle data generated by automatic measurements relating to biological characteristics of an individual that are any of the following:\n**(A)**\nFingerprints.\n**(B)**\nFacial features.\n**(C)**\nIris or retina patterns.\n**(D)**\nGait.\n**(E)**\nVoice.\n**(F)**\nBody measurements.\n**(G)**\nWeight.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Covered data**\n**(A) In general**\nThe term covered data \u2014\n**(i)**\nmeans personal data that relates to a biometric identifier, precise geolocation, or driver behavior with respect to a motor vehicle owner (or a driver or other user of a motor vehicle of such motor vehicle owner); and\n**(ii)**\nincludes personal data received by such motor vehicle from a personal device of such motor vehicle owner, driver, or other user of a motor vehicle.\n**(B) Exclusion**\nThe term covered data does not include deidentified, pseudonymous, aggregate, or publicly available information.\n**(4) Driver behavior**\nThe term driver behavior means motor vehicle data that is used for the purpose of profiling in furtherance of decisions that knowingly cause a negative legal or similarly significant harmful effect concerning the conduct of a motor vehicle owner outside the course of the employment of the motor vehicle owner.\n**(5) Motor vehicle**\nThe term motor vehicle \u2014\n**(A)**\nhas the meaning given such term in section 30102(a) of title 49, United States Code; and\n**(B)**\nincludes a motor vehicle trailer.\n**(6) Motor vehicle data**\nThe term motor vehicle data means electronic data generated or processed onboard a motor vehicle, including data generated by sensors, receivers, computer processing units, and other components of the motor vehicle.\n**(7) Motor vehicle fleet owner**\nThe term motor vehicle fleet owner \u2014\n**(A)**\nmeans a person\u2014\n**(i)**\nwith an ownership or contracted beneficial interest in 5 or more motor vehicles; or\n**(ii)**\nwho is the lessee of a motor vehicle under a lease agreement with a term of at least 180 days; and\n**(B)**\nincludes a designee of a motor vehicle owner.\n**(8) Motor vehicle owner**\nThe term motor vehicle owner \u2014\n**(A)**\nmeans an owner of a motor vehicle; and\n**(B)**\nincludes\u2014\n**(i)**\na designee of such owner;\n**(ii)**\na person with an ownership or contracted beneficial interest in a motor vehicle; and\n**(iii)**\na lessee of a motor vehicle under a lease agreement with a term of at least 180 days.\n**(9) Personal data**\nThe term personal data \u2014\n**(A)**\nmeans any motor vehicle data that is linked to an identified or identifiable natural person; and\n**(B)**\ndoes not include deidentified, pseudonymous, aggregate, or publicly available information.\n**(10) Precise geolocation**\nThe term precise geolocation means motor vehicle data that directly identifies the specific location of a natural person with precision and accuracy within a radius of 1,750 feet.\n**(11) Sell; sells; sale**\nThe terms sell , sells , and sale \u2014\n**(A)**\nmean the exchange of data for monetary consideration; and\n**(B)**\ndo not include when a driver or user of a motor vehicle requests a specific product or service from a manufacturer of a motor vehicle or a motor vehicle fleet owner that is necessary for such manufacturer or motor vehicle fleet owner to disclose such motor vehicle data to a third party to provide such service or product to such driver or user.\n**(12) User data**\nThe term user data \u2014\n**(A)**\nmeans data transferred from a personal or external device to a motor vehicle by a motor vehicle owner or user of such motor vehicle; and\n**(B)**\ndoes not include motor vehicle data.",
      "versionDate": "2025-12-12",
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
        "name": "Commerce",
        "updateDate": "2026-01-12T22:30:55Z"
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
      "date": "2025-12-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6687ih.xml"
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
      "title": "DRIVER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:54:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DRIVER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:54:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Data Rights for Information and Vehicle Electronics in Real-time Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:54:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require manufacturers of motor vehicles to provide motor vehicle owners with access to and use of motor vehicle data of motor vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:48:43Z"
    }
  ]
}
```
