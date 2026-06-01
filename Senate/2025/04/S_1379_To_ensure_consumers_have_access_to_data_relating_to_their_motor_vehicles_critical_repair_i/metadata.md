# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1379?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1379
- Title: REPAIR Act
- Congress: 119
- Bill type: S
- Bill number: 1379
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2026-02-27T12:03:21Z
- Update date including text: 2026-02-27T12:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1379",
    "number": "1379",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
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
    "title": "REPAIR Act",
    "type": "S",
    "updateDate": "2026-02-27T12:03:21Z",
    "updateDateIncludingText": "2026-02-27T12:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
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
        "item": [
          {
            "date": "2025-04-09T17:35:56Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-09T17:35:56Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "MO"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "PA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "VT"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NV"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "AZ"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "AR"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "NJ"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1379is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1379\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mr. Luj\u00e1n (for himself and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo ensure consumers have access to data relating to their motor vehicles, critical repair information, and tools, and to provide them choices for the maintenance, service, and repair of their motor vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Right to Equitable and Professional Auto Industry Repair Act or the REPAIR Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAs technology advances and vehicle systems become more advanced, vehicle repair and maintenance will require access to extensive vehicle data, software, sophisticated replacement components, training, diagnostic tools, and enhanced diagnostic repair services.\n**(2)**\nConsumers and their designees must have access to vehicle-generated data and alternative parts that are necessary to maintain consumer choice and competitive pricing.\n**(3)**\nConsumer choice, consumer control, motor vehicle cybersecurity, and safety are all valid concerns and do not have to be mutually exclusive.\n**(4)**\nVehicles generate increasingly massive amounts of data and the Federal Trade Commission and the National Highway Traffic Safety Administration are uniquely positioned, after considering consumers\u2019 privacy and cybersecurity needs, to designate additional types of data not specifically considered or identified by Congress that consumers should be able to easily share with persons they choose for the reasons they choose and examine fair competition in evolving motor vehicle technologies.\n**(5)**\nIt is in the interest of the United States to foster competition in the motor vehicle repair industry and not limit consumers in their choices for maintenance, service, and repair, allowing consumers and the industry to benefit from a system that fosters communication, collaboration, and innovation and promotes consumer choice.\n#### 3. Definitions\n##### (a) Definitions\nIn this Act:\n**(1) Aftermarket part**\nThe term aftermarket part means a new part for a motor vehicle that\u2014\n**(A)**\nis not original equipment and is sold or offered for sale to a motor vehicle manufacturer after the vehicle has left the motor vehicle manufacturer's production line; or\n**(B)**\nwas manufactured for a person that is not the motor vehicle manufacturer.\n**(2) Alternative part**\n**(A) In general**\nThe term alternative part \u2014\n**(i)**\nmeans any part for a motor vehicle offered for sale or for installation in or on a motor vehicle, or manufactured for sale to a motor vehicle manufacturer, after such motor vehicle has left the motor vehicle manufacturer\u2019s production line; and\n**(ii)**\nincludes aftermarket parts, recycled parts, and remanufactured parts.\n**(B) Exclusions**\nThe term alternative part shall not include any original equipment.\n**(3) Authorized motor vehicle service provider**\nThe term authorized motor vehicle service provider means a person who has\u2014\n**(A)**\nan arrangement with a motor vehicle manufacturer under which the motor vehicle manufacturer grants to the person a license to use a trade name, service mark, or other proprietary identifier for the purpose of offering the service of diagnosis, maintenance, or repair of a motor vehicle under the name of the motor vehicle manufacturer; or\n**(B)**\nany other arrangement with the motor vehicle manufacturer to offer such services on behalf of the motor vehicle manufacturer.\n**(4) Barrier**\nThe term barrier means a technological or contractual restriction that prohibits or materially interferes with the ability of a motor vehicle repair facility or a service provider to return a vehicle to operational specifications, including any action that prohibits or materially interferes with the process of pairing aftermarket parts or alternative parts with the vehicle.\n**(5) Commission**\nThe term Commission means the Federal Trade Commission.\n**(6) Critical repair information, tools, and parts**\nThe term critical repair information, tools, and parts means all necessary technical and compatibility information, tools, and motor vehicle equipment made available by a motor vehicle manufacturer to a motor vehicle dealer or a motor vehicle repair facility, or used by the motor vehicle manufacturer, for the purpose of maintaining or repairing a motor vehicle, wiring diagrams, parts nomenclature and descriptions, parts catalogs, repair procedures, training materials, software, and technology, including information related to diagnostics, repair, service, calibration, or recalibration of parts and systems to return a vehicle to operational specifications.\n**(7) Diagnostic tool manufacturer**\nThe term diagnostic tool manufacturer means a person who develops and manufactures any electronic tool (or software for such tool) that connects to a motor vehicle's computer or electronic control modules in order to download or access vehicle diagnostic trouble codes or reprogram the motor vehicle\u2019s computer or electronic control modules to return the motor vehicle to its original operating state.\n**(8) Distributor**\nThe term distributor means a person that buys any motor vehicle equipment or diagnostic tool from a manufacturer and sells them to other businesses, stores, or customers.\n**(9) Insurer**\nThe term insurer has the meaning given that term under section 313(r) of title 31, United States Code, as term applies to automobile insurance.\n**(10) Junk yard; salvage yard**\nThe terms junk yard and salvage yard have the meanings given those terms in section 25.52 of title 28, Code of Federal Regulations as in effect on September 1, 2021.\n**(11) Motor vehicle**\nThe term motor vehicle has the meaning given such term in section 30102(a) of title 49, United States Code, and includes a motor vehicle trailer.\n**(12) Motor vehicle dealer**\nThe term motor vehicle dealer has the meaning given to the term dealer in section 30102(a) of title 49, United States Code.\n**(13) Motor vehicle equipment**\nThe term motor vehicle equipment has the meaning given such term in section 30102(a) of title 49, United States Code.\n**(14) Motor vehicle manufacturer**\nThe term motor vehicle manufacturer has the meaning given such term in section 30102(a) of title 49, United States Code.\n**(15) Motor vehicle owner**\n**(A) In general**\nThe term motor vehicle owner means\u2014\n**(i)**\na person with a present possessive ownership right in a motor vehicle; or\n**(ii)**\na lessee of a motor vehicle.\n**(B) Exclusions**\nThe term motor vehicle owner shall not include a motor vehicle manufacturer or a person operating on behalf of a motor vehicle manufacturer, a motor vehicle financing company, a motor vehicle dealer, or a motor vehicle lessor.\n**(16) Motor vehicle repair facility**\nThe term motor vehicle repair facility means any person who, in its ordinary course of business, is engaged in the business of diagnosis, service, maintenance, repair, or calibration of motor vehicles or motor vehicle equipment.\n**(17) Original equipment**\nThe term original equipment means motor vehicle equipment (including a tire) that, as of the time of delivery to the first motor vehicle owner, is installed in or on a motor vehicle.\n**(18) Person**\nThe term person means an individual, trust, estate, partnership, association, company, or corporation.\n**(19) Recycled part**\nThe term recycled part means any part offered for sale or for installation in or on a motor vehicle that was previously installed in or on a different motor vehicle.\n**(20) Remanufacturer**\nThe term remanufacturer means a person utilizing a standardized industrial process\u2014\n**(A)**\nby which previously sold, worn, or non-functional products are returned to same-as-new, or better, condition and performance;\n**(B)**\nthat is in line with specific technical specifications, including engineering, quality, and testing standards; and\n**(C)**\nthat yields fully warranted products.\n**(21) Remanufactured part**\nThe term remanufactured part means a part for a motor vehicle produced by a remanufacturer.\n**(22) Service provider**\nThe term service provider means\u2014\n**(A)**\nany motor vehicle repair facility (or other designee) who is employed by a motor vehicle owner to assist with the diagnosis and repair of a motor vehicle (including wireless and remote technologies) or with any other wireless and remote services comparable to those provided by a vehicle manufacturer;\n**(B)**\na motor vehicle dealer; or\n**(C)**\nan authorized motor vehicle service provider.\n**(23) Telematics system**\nThe term telematics system means any system in a motor vehicle that collects information generated by the operation of the vehicle and transmits such information utilizing wireless communications to a remote receiving point where the information is stored.\n**(24) Vehicle-generated data**\nThe term vehicle-generated data means any in-vehicle data generated (or generated and retained) by the operation of a motor vehicle related to diagnostics, prognostics, repair, service, wear, calibration, or recalibration of parts or systems required to return a vehicle to operational specifications in compliance with Federal motor vehicle safety and emissions laws, regulations, and standards.\n##### (b) Authority To expand definitions\nThe Commission, in consultation with the National Highway Traffic Safety Administration, may promulgate regulations in accordance with section 553 of title 5, United States Code, to expand the definitions under this section, as determined necessary by the Commission.\n#### 4. Maintaining competition after consumers purchase or lease their motor vehicles\n##### (a) In general\n**(1) Prohibition on restricting the ability of motor vehicle owners to use the repair parts and repair facilities of their choice**\nBeginning on the date that is 180 days after the date of enactment of this Act:\n**(A) Use of barriers**\nA motor vehicle manufacturer shall not employ any barrier that impairs the ability of\u2014\n**(i)**\na motor vehicle owner (or their designee) to access vehicle-generated data;\n**(ii)**\na motor vehicle owner (or their designee), an aftermarket parts manufacturer, a motor vehicle equipment manufacturer, a remanufacturer, a diagnostic tool manufacturer, or a motor vehicle repair facility (including their distributors and service providers), to access critical repair information, tools, and parts;\n**(iii)**\na motor vehicle owner (or their designee) to use a vehicle towing or service provider of their choice;\n**(iv)**\nan aftermarket parts manufacturer, a motor vehicle equipment manufacturer, a remanufacturer, a junk yard, a salvage yard, or a motor vehicle repair facility (including their distributors and service providers) to produce or offer compatible alternative parts;\n**(v)**\na motor vehicle owner (or their designee) to install and use compatible alternative parts in or on a motor vehicle to repair or maintain the motor vehicle; or\n**(vi)**\na motor vehicle owner (or their designee) to diagnose, repair, or maintain a motor vehicle.\n**(B) Software updates**\nSubject to paragraph (5), a motor vehicle manufacturer shall not intentionally implement, while addressing driver and operational safety, any software update to a motor vehicle with the specific intent of rendering any compatible alternative part or aftermarket part inoperable, in whole or in part, except as required by an order issued by the National Highway Traffic Safety Administration.\n**(2) Requirement to provide vehicle-generated data to motor vehicle owners and their designees**\nBeginning on the date that is 180 days after the date of enactment of this Act, a motor vehicle manufacturer shall\u2014\n**(A)**\nprovide to a motor vehicle owner (or their designee), without restriction or limitation, access to vehicle-generated data, including vehicle-generated data made available through the motor vehicle's interface ports; and\n**(B)**\nto the extent the motor vehicle is equipped for wireless transmission of vehicle-generated data over wireless technology via any telematics system, provide to a motor vehicle owner (or their designee) access to their vehicle-generated data\u2014\n**(i)**\nat a fair, reasonable, and nondiscriminatory cost in or at the same manner, sequence, and method as any motor vehicle manufacturer, affiliate of a motor vehicle manufacturer, motor vehicle dealer, authorized motor vehicle service provider, or any other third party to which a motor vehicle manufacturer gives vehicle-generated data has access to such data; and\n**(ii)**\nin a manner that is subject to the same cryptographic or technological protections as any motor vehicle manufacturer, affiliate of a motor vehicle manufacturer, motor vehicle dealer, authorized motor vehicle service provider, or any other third party to whom the motor vehicle manufacturer provides such data.\n**(3) Requirement to make critical repair information, tools, and parts available for purchase by motor vehicle owners, designees of motor vehicle owners, and members of the repair industry**\nBeginning on the date that is 180 days after the date of enactment of this Act, a motor vehicle manufacturer shall make available to motor vehicle owners (and their designees), aftermarket parts manufacturers, remanufacturers, diagnostic tool manufacturers, and motor vehicle repair facilities (including their distributors and service providers), without restrictions or limitations, any critical repair information, tools, and parts related to the motor vehicles it manufactures at a fair, reasonable, and non-discriminatory cost.\n**(4) Prohibition on certain mandates by motor vehicle manufacturers related to repairs**\n**(A) In general**\nSubject to subparagraph (B), a motor vehicle manufacturer shall not, within any repair or maintenance service procedure, recommendation, service bulletin, repair manual, position statement, software, firmware, other electronic system, or other similar repair or maintenance guide that is distributed to consumers or to professional repairers\u2014\n**(i)**\nmandate the use of any particular brand or manufacturer of tools, parts, or other motor vehicle equipment;\n**(ii)**\nprohibit the use of alternative parts to repair or maintain a motor vehicle; or\n**(iii)**\nrecommend the use of any particular brand or manufacturer of tools, parts, or other motor vehicle equipment unless the motor vehicle manufacturer provides a prominent notice immediately following the recommendation, in the same font as the recommendation and in a font size no smaller than the font size used in the recommendation, stating that: Vehicle owners can choose which repair tools, parts, and other motor vehicle equipment to purchase and should carefully consider their options among different brands and manufacturers. .\n**(B) Exception**\nThe prohibition described in subparagraph (A) shall not apply to a recall, warranty repair, or voluntary repair campaign.\n**(5) Cybersecurity**\nNothing in this section shall preclude a motor vehicle manufacturer from employing cryptographic or technological protections necessary to secure vehicle-generated data, safety critical vehicle systems, and vehicles, provided that such protections comply with the requirements described in paragraphs (1) and (2).\n**(6) Designee prohibitions**\nA motor vehicle manufacturer\u2014\n**(A)**\nshall not limit the number or type of persons that a motor vehicle owner may designate as simultaneous designees; and\n**(B)**\nshall ensure that a motor vehicle owner has the ability to revoke the designation of a person as a designee in the same manner as the motor vehicle owner designated such person as a designee.\n**(7) Required notification**\nEach motor vehicle manufacturer shall provide a notification, using an on-vehicle screen or through a mobile device, to a motor vehicle owner when the vehicle-generated data of the owner is being accessed by any designee of the owner.\n##### (b) Nullification of attempts To restrict competition and consumer rights\nAny provision in a contract executed on or after the date of enactment of this Act by or on behalf of a motor vehicle manufacturer that purports to violate subsection (a) shall be null and void to the extent that it would allow the motor vehicle manufacturer to avoid its obligations under subsection (a).\n##### (c) Proprietary interfaces\nNothing in this section shall be construed\u2014\n**(1)**\nto require a motor vehicle dealer to use a non-proprietary vehicle interface; or\n**(2)**\nto prohibit a motor vehicle manufacturer from developing a proprietary vehicle diagnostic and reprogramming device, provided that the motor vehicle manufacturer\u2014\n**(A)**\notherwise complies with the requirements of this section; and\n**(B)**\nmakes any such proprietary device available to all motor vehicle repair facilities and parts and tool manufacturers upon fair and reasonable terms.\n#### 5. Fair competition after vehicles are sold advisory committee\n##### (a) Establishment\nNot later than 90 days after the date of enactment of this Act, the Commission shall establish a Fair Competition After Vehicles Are Sold Advisory Committee (in this section referred to as the Advisory Committee ) to provide recommendations to the Commission regarding the implementation of this Act and best practices to eliminate any barriers to competition in the motor vehicle repair industry, including an assessment of such existing and emerging barriers, as well as ensuring motor vehicle owners' control over their vehicle-generated data.\n##### (b) Membership\n**(1) In general**\nThe Advisory Committee shall be composed of the following members:\n**(A)**\nThe Director of the Bureau of Competition.\n**(B)**\nThe Administrator of the National Highway Traffic Safety Administration.\n**(C)**\nEleven individuals, appointed by the Chair of the Commission, from each of the following:\n**(i)**\nIndependent repair facilities.\n**(ii)**\nMotor vehicle parts retailers.\n**(iii)**\nMotor vehicle parts distributors.\n**(iv)**\nOriginal equipment parts manufacturers.\n**(v)**\nAftermarket parts manufacturers.\n**(vi)**\nDiagnostic tool manufacturers.\n**(vii)**\nMotor vehicle manufacturers.\n**(viii)**\nVehicle dealership service centers.\n**(ix)**\nConsumer rights organizations.\n**(x)**\nAutomobile insurers.\n**(xi)**\nTrucking companies.\n**(2) Chair**\nThe Chair of the Commission shall serve as the Chair of the Advisory Committee.\n##### (c) Duties\nThe Advisory Committee shall\u2014\n**(1)**\nprovide recommendations to the Commission regarding fostering industry collaboration in a clear and transparent manner;\n**(2)**\ncoordinate with and include participation by the private sector (including each industry described in subsection (b)(1)(C)), members of the public, and other interested parties; and\n**(3)**\nassess existing and emerging barriers to competitive motor vehicle repair.\n##### (d) Meetings\nThe Advisory Committee shall meet at least 3 times per year at the call of the Chair.\n##### (e) Reports\n**(1) Report to the Chair**\nNot later than 180 days after the first meeting of the Advisory Committee, and annually thereafter, the Advisory Committee shall submit to the Chair a report on efforts by each industry described in subsection (b)(1)(C) to implement this Act, as well as an assessment of any existing and emerging barriers to motor vehicle repair and motor vehicle owners\u2019 control over their vehicle-generated data.\n**(2) Report to Congress**\nNot later than 30 days after receiving a report under paragraph (1), the Commission shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a copy of such report, together with recommendations for such legislative or administrative action as the Commission determines appropriate.\n##### (f) Termination\nThe Advisory Committee shall terminate upon an agreement of a majority of the membership, but in no case earlier than 1 year after the first meeting of the Advisory Committee. The Advisory Committee shall provide notice of its planned termination to Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives, not later than 30 days prior to such termination and shall include a basis for the termination.\n#### 6. Rulemaking\n##### (a) Security standards for access to vehicle-Generated data\nNot later than 1 year after the date of enactment of this Act, the Administrator of the National Highway Traffic Safety Administration, in consultation with the National Institute of Standards and Technology, shall promulgate regulations in accordance with section 553 of title 5, United States Code, to establish\u2014\n**(1)**\nstandards for consumer access to vehicle-generated data in accordance with section 4(a)(2); and\n**(2)**\nprocedures to ensure the security of vehicle-generated data and motor vehicles as related to the access of vehicle-generated data required under this Act.\n##### (b) Consumer notification\nNot later than 2 years after the date of enactment of this Act, the Commission, in coordination with the Administrator of the National Highway Traffic Safety Administration, shall promulgate regulations in accordance with section 553 of title 5, United States Code, to require motor vehicle manufacturers and motor vehicle dealers to inform motor vehicle owners of their rights under this Act at the point of purchase or lease of a motor vehicle.\n#### 7. Enforcement by the Commission\n##### (a) Unfair or deceptive acts or practices\nA violation of section 4(a) or a regulation promulgated under this Act shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n##### (b) Powers of the Commission\n**(1) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(2) Privileges and immunities**\nAny person who violates this Act or a regulation promulgated thereunder shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n**(4) Rulemaking**\nThe Commission shall promulgate in accordance with section 553 of title 5, United States Code, such rules as may be necessary to carry out this Act.\n#### 8. Consumer complaints\n##### (a) In general\nNot later than 90 days after the date of enactment of this Act, the Commission shall establish a mechanism to receive complaints regarding alleged violations of this Act by a motor vehicle manufacturer.\n##### (b) Notification to and response from a motor vehicle manufacturer\nUpon receiving a complaint though the mechanism established under subsection (a), the Commission shall forward the complaint to the motor vehicle manufacturer named in the complaint, and request that such motor vehicle manufacturer answer the complaint in writing within a reasonable time, as specified by the Commission, but in no case shall such time period exceed 30 days from the motor vehicle manufacturer\u2019s receipt of the complaint.\n##### (c) Investigation by the Commission\n**(1) In general**\nIf the motor vehicle manufacturer does not answer within the time period specified by the Commission under subsection (b), the Commission shall investigate the matters complained of in such manner and by such means as the Commission shall consider proper.\n**(2) Special rule**\nIn investigating a complaint under this section, the Commission may not dismiss such complaint due to the absence of direct damage to the person submitting such complaint.\n**(3) Deadline for orders by the Commission**\nThe Commission shall, with respect to any investigation of complaint of a violation of this Act or a regulation promulgated thereunder, issue an order concluding such investigation within 5 months after the date on which the complaint was filed. Any order concluding an investigation under this paragraph shall be a final order and may be appealed to the United States District Court for the District of Columbia.\n#### 9. Report to Congress\nNot later than 2 years after the date of enactment of this Act, and biennially thereafter, the Commission shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that includes\u2014\n**(1)**\na summary of investigations conducted and orders issued under section 8, including\u2014\n**(A)**\na description of any unfair practice relating to repair and data access restrictions; and\n**(B)**\na summary of best practices from stakeholders; and\n**(2)**\na description of any action the Commission is taking to\u2014\n**(A)**\nadapt to changes and advances in motor vehicle technology to maintain competition in the motor vehicle aftermarket; and\n**(B)**\nensure motor vehicle owners\u2019 control over their vehicle-generated data.\n#### 10. Relationship with other laws\n##### (a) Preemption of other State laws\nNo State or political subdivision of a State may adopt, maintain, enforce, impose, or continue in effect a law, regulation, rule, standard, prohibition, requirement, or other provision having the force and effect of law that is covered by the provisions of this Act, or a rule, regulation, or requirement promulgated under this Act.\n##### (b) Field preemption\nThis Act shall preempt any State law, rule, or regulation that mandates the use of any particular brand or manufacturer of tools, parts, or other motor vehicle equipment, or prohibits the use of any aftermarket parts, recycled parts, or remanufactured parts solely on the basis of such parts being aftermarket parts, recycled parts, or remanufactured parts, for the purpose of maintaining, diagnosing, or repairing a motor vehicle.\n#### 11. Severability\nIf any provision of this Act, or the application thereof to any person or circumstance, is held invalid, the remainder of this Act, and the application of such provision to other persons not similarly situated or to other circumstances, shall not be affected by the invalidation.",
      "versionDate": "2025-04-09",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-19T16:06:06Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1379is.xml"
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
      "title": "REPAIR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-27T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "REPAIR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Right to Equitable and Professional Auto Industry Repair Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure consumers have access to data relating to their motor vehicles, critical repair information, and tools, and to provide them choices for the maintenance, service, and repair of their motor vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T03:18:19Z"
    }
  ]
}
```
