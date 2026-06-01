# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7741?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7741
- Title: E-Access Act
- Congress: 119
- Bill type: HR
- Bill number: 7741
- Origin chamber: House
- Introduced date: 2026-02-26
- Update date: 2026-04-24T20:08:24Z
- Update date including text: 2026-04-24T20:08:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-26: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-26: Introduced in House

## Actions

- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7741",
    "number": "7741",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "E-Access Act",
    "type": "HR",
    "updateDate": "2026-04-24T20:08:24Z",
    "updateDateIncludingText": "2026-04-24T20:08:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-26",
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
      "actionDate": "2026-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-26",
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
          "date": "2026-02-26T14:31:45Z",
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
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7741ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7741\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2026 Mr. Mullin (for himself and Mr. Levin ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo promote competition in the area of digital energy management tools, enhance consumer access to electric energy and natural gas information, allow for the development and adoption of innovative products and services to help consumers, organizations, and governments manage their energy usage and improve electric grid reliability, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Access to Consumer Energy Information Act or the E-Access Act .\n#### 2. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Energy Regulatory Commission.\n**(2) Covered wholesale electricity market**\nThe term covered wholesale electricity market means a wholesale electricity market regulated by, or otherwise subject to the jurisdiction of, the Federal Energy Regulatory Commission.\n**(3) Electric consumer**\nThe term electric consumer has the meaning given the term in section 3 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2602 ).\n**(4) Electric meter software platform**\nThe term electric meter software platform means the meter of an electric utility and any accompanying software that enables software applications to be developed, installed, and executed on the grid edge computer for the purpose of analyzing or transmitting retail electric energy information or grid edge consumer insights.\n**(5) Electric utility**\nThe term electric utility has the meaning given the term in section 3 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2602 ).\n**(6) Gas consumer**\nThe term gas consumer has the meaning given the term in section 302 of the Public Utility Regulatory Policies Act of 1978 ( 15 U.S.C. 3202 ).\n**(7) Gas utility**\nThe term gas utility has the meaning given the term in section 302 of the Public Utility Regulatory Policies Act of 1978 ( 15 U.S.C. 3202 ).\n**(8) Green button connect my data**\nThe term Green Button Connect My Data means the standard of the same name that is maintained by the Green Button Alliance (or any successor organization) that enables access to and secure transmission of retail electric energy information and retail natural gas information by an electric consumer or gas consumer, including any subsequent updates to the standard or successor standards.\n**(9) Grid edge computer**\nThe term grid edge computer means a device, whether part of, or separate from, a meter, that\u2014\n**(A)**\nmeasures power, voltage, current, or other aspects of electric energy at or near the premises of an electric consumer; and\n**(B)**\nis capable of running 1 or more software applications to analyze, in real time, any measurement described in subparagraph (A) in order to derive grid edge consumer insights or information about the status or operation of the electric grid.\n**(10) Grid edge consumer insight**\nThe term grid edge consumer insight means\u2014\n**(A)**\nthe power, voltage, current, or other aspects of electric energy measured and analyzable by a grid edge computer; and\n**(B)**\nany calculation, estimate, or inference from a grid edge computer that pertains to, or reflects the characteristics of, the use of electric energy by a particular electric consumer.\n**(11) Independent System Operator**\nThe term Independent System Operator has the meaning given the term in section 3 of the Federal Power Act ( 16 U.S.C. 796 ).\n**(12) Meter**\nThe term meter means a device that measures and records energy usage data at any interval.\n**(13) Regional Transmission Organization**\nThe term Regional Transmission Organization has the meaning given the term in section 3 of the Federal Power Act ( 16 U.S.C. 796 ).\n**(14) Retail electric energy information**\nThe term retail electric energy information means\u2014\n**(A)**\nthe electric energy usage of an electric consumer over a time interval, as measured and recorded by the applicable meter;\n**(B)**\nthe retail electric energy prices and applicable rate applied to the electric energy usage for the time interval described in subparagraph (A) for the electric consumer;\n**(C)**\nthe costs of service provided to an electric consumer, as displayed on billing information provided to that electric consumer at the level of each line item;\n**(D)**\nin the case of nonresidential electric meters, any other electrical information that the meter is programmed to record that is used for billing purposes (such as demand measured in kilowatts, voltage, frequency, current, and power factor);\n**(E)**\ngrid edge consumer insights; and\n**(F)**\ncustomer-specific information including, at a minimum\u2014\n**(i)**\ncustomer name, mailing address, premises address, contact information, payment history, and account number; and\n**(ii)**\nany information that may be necessary for participation in, or to determine customer eligibility for, bill payment assistance, renewable energy, demand-side management, load management, energy efficiency programs, or wholesale markets.\n**(15) Retail natural gas information**\nThe term retail natural gas information means\u2014\n**(A)**\nthe natural gas usage of a gas consumer, as measured and recorded by the applicable gas utility;\n**(B)**\nthe retail natural gas prices and applicable rate applied to the natural gas usage described in subparagraph (A) for the gas consumer;\n**(C)**\nthe cost of service provided to a gas consumer, as displayed on billing information provided to that gas consumer at the level of each line item;\n**(D)**\nin the case of nonresidential natural gas meters, any other information that the meter is programmed to record that is used for billing purposes; and\n**(E)**\ncustomer-specific information including, at a minimum\u2014\n**(i)**\ncustomer name, mailing address, premises address, contact information, payment history, and account number; and\n**(ii)**\nany information that might be necessary for participation in, or to determine customer eligibility for, bill payment assistance, demand-side management, energy efficiency programs, or wholesale markets.\n**(16) Secretary**\nThe term Secretary means the Secretary of Energy.\n**(17) State energy office**\nThe term State energy office means the office or agency of a State responsible for developing the State energy conservation plan for the State under section 362 of the Energy Policy and Conservation Act ( 42 U.S.C. 6322 ).\n#### 3. Consumer access to electric energy and natural gas information\n##### (a) Eligibility for State energy plans\nSection 362(d) of the Energy Policy and Conservation Act ( 42 U.S.C. 6322(d) ) is amended\u2014\n**(1)**\nin paragraph (17), by striking and after the semicolon at the end;\n**(2)**\nby redesignating paragraph (18) as paragraph (19); and\n**(3)**\nby inserting after paragraph (17) the following:\n(18) programs to promote competition in the area of digital energy management tools\u2014 (A) to enhance consumer access to, and understanding of, electric energy and natural gas usage and cost information, including, with respect to each particular customer\u2014 (i) the residential and commercial retail electric energy information (as defined in section 2 of the E-Access Act ) of that customer; and (ii) the retail natural gas information (as defined in that section) of that customer; (B) to facilitate the development and adoption of innovative products and services to assist consumers in managing energy consumption and expenditures; and (C) to increase the adoption of measured, performance-based energy efficiency and demand response programs; and .\n##### (b) Guidelines for electric consumer and gas consumer data access\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act and subject to paragraph (2), the Secretary and the Commission shall jointly develop and issue guidelines that establish model data sharing standards and policies for States to provide electric consumers and gas consumers, and third-party designees of those electric consumers and gas consumers, with access to retail electric energy information and retail natural gas information.\n**(2) Consultation**\nBefore issuing guidelines under paragraph (1), the Secretary shall\u2014\n**(A)**\nconsult with\u2014\n**(i)**\nState and local regulatory authorities;\n**(ii)**\nother appropriate Federal agencies, including the National Institute of Standards and Technology and the Federal Trade Commission;\n**(iii)**\nconsumer and privacy advocacy groups;\n**(iv)**\nelectric utilities and gas utilities;\n**(v)**\nthe National Association of State Energy Officials; and\n**(vi)**\nother appropriate entities, including groups representing public utility commissions, commercial and residential building owners, residential contractors, and groups that represent demand response and electricity data devices and services; and\n**(B)**\nprovide notice and opportunity for comment.\n**(3) State and local regulatory action**\nIn issuing guidelines under paragraph (1), the Secretary, to the maximum extent practicable, shall be guided by actions taken by State and local regulatory authorities to ensure electric consumer and gas consumer access to retail electric energy information and retail natural gas information, including actions taken after consideration of the standard established under section 111(d)(19) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2621(d)(19) ).\n**(4) Contents**\nIn carrying out paragraph (1), the Secretary shall include\u2014\n**(A)**\nguidelines specifying that retail electric energy information and retail natural gas information of an electric consumer or a gas consumer should be made available to the electric consumer or gas consumer (or a third-party designee of the electric consumer or gas consumer) by the electric utility or gas utility of the electric consumer or gas consumer (or such other entity as may be designated by the utility), in consultation with, or with approval from, as applicable, the applicable retail regulatory authority of the utility;\n**(B)**\nguidelines regarding the timeliness and specificity of retail electric energy information and retail natural gas information to be made available to an electric consumer or a gas consumer (or a third-party designee of an electric consumer or a gas consumer), including that the retail electric energy information and retail natural gas information should be made available\u2014\n**(i)**\nin an electronic machine-readable form, without additional charge, in conformity with nationally recognized open standards and best practices;\n**(ii)**\nvia a website or other electronic access authorized by the electric consumer or gas consumer, including at least 24 months of historical information;\n**(iii)**\nin as close to real-time as is reasonably practicable;\n**(iv)**\nat the level of specificity that the data are transmitted by the meter or grid edge computer, to the extent reasonably practicable; and\n**(v)**\nin a manner that provides adequate protections for the security of the information and the privacy of the electric consumer or gas consumer, utilizing recognized energy data privacy programs such as the DataGuard Energy Data Privacy Program of the Department of Energy or other programs approved by the Secretary;\n**(C)**\nguidelines regarding appropriate nationally recognized open standards for data exchange;\n**(D)**\nguidelines regarding consumer consent requirements to ensure that an electric consumer or gas consumer can conveniently and securely authorize a third-party designee to access the retail electric energy information or retail natural gas information of that electric consumer or gas consumer, including standardized authorization language to which an electric consumer or gas consumer will agree prior to the electric consumer or gas consumer authorizing, or the applicable electric utility or gas utility sharing, retail electric energy information or retail natural gas information of that electric consumer or gas consumer;\n**(E)**\nguidelines specifying that electric utilities and gas utilities should, when a meter is servicing an electric consumer or gas consumer, communicate retail electric energy information or retail natural gas information to the device of the electric consumer or gas consumer or through the network of an electric consumer or gas consumer to a third-party designee of the electric consumer or gas consumer;\n**(F)**\nwith respect to the terms and conditions to be agreed to by a third-party designee of an electric consumer or a gas consumer and an electric utility or a gas utility for access to the retail electric energy information or retail natural gas information of that electric consumer or gas consumer, guidelines specifying that\u2014\n**(i)**\nthose terms and conditions shall be reasonable and nondiscriminatory;\n**(ii)**\nthose terms and conditions shall not require anything of a third-party designee beyond requiring\u2014\n**(I)**\nthe third-party designee to provide to the electric utility or gas utility\u2014\n**(aa)**\nthe contact information and Federal tax identification number of the third-party designee; and\n**(bb)**\nan acknowledgment of compliance with a privacy requirement, such as the DataGuard Energy Data Privacy Program of the Department of Energy; and\n**(II)**\nthat the third-party designee has not been disqualified by the applicable retail regulatory authority of the utility;\n**(iii)**\ndue process shall be afforded to the third-party designee by the applicable regulatory authority, including by giving the third-party designee an opportunity to rebut allegations of wrongdoing by that third-party designee prior to any enforcement action being taken by the applicable regulatory authority;\n**(iv)**\nthe online authorization process offered by the applicable gas utility or electric utility to the consumer shall be user-friendly, and the personal information required to establish identity shall be consistent with, and no more onerous than, the standard practices of the applicable gas utility or electric utility; and\n**(v)**\nthe third party may receive retail electric energy information and retail natural gas information from an electric utility or gas utility with consumer consent, except if otherwise prohibited by Federal law or by a finding of a State court or other State adjudicatory body;\n**(G)**\nguidelines specifying that electric utilities and gas utilities shall, on a periodic basis as recommended by the Secretary, provide certification by an independent body of adherence to the latest Green Button Connect My Data or another, similar, standard;\n**(H)**\nguidelines specifying that Green Button Connect My Data system availability, as provided by electric utilities and gas utilities, shall exceed 99-percent availability without severe errors or defects;\n**(I)**\nguidelines specifying that electric utilities and gas utilities shall report on a publicly available website the timeliness and performance of the processing of electronic data-sharing authorizations and the timeliness of completing third-party administrative and technical onboarding with an electric utility or gas utility, including recommendations from the Secretary as to whether electric utilities and gas utilities, or State or Federal agencies, should host such publicly available websites;\n**(J)**\nguidelines specifying that\u2014\n**(i)**\nan electric meter software platform shall\u2014\n**(I)**\nhave terms that are fair, reasonable, and nondiscriminatory to any authorized user;\n**(II)**\ntransparently disclose uptime, performance, and availability; and\n**(III)**\ntransparently disclose the timelines and procedures for evaluating new software applications submitted for deployment on the platform;\n**(ii)**\nsoftware developers and distributed energy resources that use electric meter software platforms or retail electric customer information shall\u2014\n**(I)**\nhave access to platform software documentation; and\n**(II)**\nbe afforded due process rights with regard to disputes concerning functionality or availability;\n**(iii)**\nowners or operators of electric meter software platforms shall address fair competition issues, including self-preferencing, surveillance of competitive software applications, and undue use of default software applications that have the effect of reducing consumer choices; and\n**(iv)**\nelectric consumers, gas consumers, electric utilities, and gas utilities shall have the right to select, install, and operate applications of their choosing on the electric meter, subject to reasonable technical requirements; and\n**(K)**\nguidelines addressing appropriate circumstances in which analysis of retail electric energy information, retail natural gas information, and estimates of energy saved as a result of any efficiency measure may be released publicly, without the consent of the consumer, only by protection of individual consumer privacy via mathematical methods such as differential privacy, or by alternative means at the discretion of the Secretary, if required, that prevent reidentification of the attributes of individual consumers when publishing aggregate information.\n**(5) Revisions**\nEvery 3 years, the Secretary shall review and, as necessary, revise the guidelines issued under paragraph (1) to reflect changes in technology, privacy needs, and the market for electric energy and natural gas and related services.\n##### (c) Verification and implementation\n**(1) In general**\nA State energy office may submit to the Secretary a description of the policies of the State relating to electric consumer and gas consumer access to retail electric energy information and retail natural gas information for certification by the Secretary that the policies meet the guidelines issued under subsection (b).\n**(2) Assistance**\nSubject to the availability of amounts appropriated pursuant to paragraph (3), the Secretary shall make amounts available to any State that has policies described in paragraph (1) that the Secretary certifies meet the guidelines issued under subsection (b) to assist the State in implementing programs described in paragraph (18) of section 362(d) of the Energy Policy and Conservation Act ( 42 U.S.C. 6322(d) ) (as amended by subsection (a)).\n**(3) Authorization of appropriations**\nThere is authorized to be appropriated to carry out this subsection $10,000,000 for fiscal year 2026, to remain available until expended.\n##### (d) Report on accurate electric meter settlement\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary and the Commission shall jointly develop and submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Energy and Commerce of the House of Representatives a report evaluating the costs and benefits of electric utilities transmitting meter data for each individual electric consumer to covered wholesale electricity markets for the purpose of settling market prices.\n**(2) Inclusions**\nThe report submitted under paragraph (1) shall include\u2014\n**(A)**\nthe number of customers of electric utilities across the United States served by advanced metering infrastructure;\n**(B)**\nthe number of customers and the associated capacity of megawatts of flexible electricity demand that lack access to, or settlement on, electric meter data;\n**(C)**\ncase studies of regions across the United States in which electric meter data is used for settling covered wholesale electricity market purchases, including best practices;\n**(D)**\nan analysis of potential anticompetitive impacts of denying customers of electric utilities access to electric meter data, which may include impacts from preventing the aggregation or transmission of electric meter data for the purposes of settling covered wholesale electricity market purchases;\n**(E)**\nan estimate of the amount of taxpayer and electric ratepayer dollars spent on electric metering and supporting systems associated with restructured retail markets that do not settle covered wholesale electricity market purchases based on electric meter data;\n**(F)**\nan estimate of the number of customers of electric utilities that are unable to participate in demand-side covered wholesale electricity market programs because the applicable electric meter is not programmed at the necessary time intervals;\n**(G)**\nan estimate of the reasonably foreseeable costs that electric utilities would incur to reprogram electric meters\u2014\n**(i)**\nto participate in demand-side covered wholesale electricity market programs; and\n**(ii)**\nto match the requirements of operators of relevant covered wholesale electricity markets with respect to the use of demand-side resources;\n**(H)**\nan estimate of the reasonably foreseeable costs that electric utilities, Independent System Operators, and Regional Transmission Organizations would incur in settling covered wholesale electricity market purchases based on electric meter data; and\n**(I)**\nan analysis of potential benefits to reliability, customer choice, and technology availability that may result from settling covered wholesale electricity market purchases based on electric meter data.",
      "versionDate": "2026-02-26",
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
        "actionDate": "2026-02-26",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "3926",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "E-Access Act",
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
        "name": "Energy",
        "updateDate": "2026-04-24T20:08:24Z"
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
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7741ih.xml"
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
      "title": "E-Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-22T06:53:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "E-Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-22T06:53:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Access to Consumer Energy Information Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-22T06:53:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To promote competition in the area of digital energy management tools, enhance consumer access to electric energy and natural gas information, allow for the development and adoption of innovative products and services to help consumers, organizations, and governments manage their energy usage and improve electric grid reliability, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-22T06:47:20Z"
    }
  ]
}
```
