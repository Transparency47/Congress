# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4557?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4557
- Title: Outage Refund Protection Act
- Congress: 119
- Bill type: S
- Bill number: 4557
- Origin chamber: Senate
- Introduced date: 2026-05-18
- Update date: 2026-05-29T07:38:44Z
- Update date including text: 2026-05-29T07:38:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-18: Introduced in Senate
- 2026-05-18 - IntroReferral: Introduced in Senate
- 2026-05-18 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-05-18: Introduced in Senate

## Actions

- 2026-05-18 - IntroReferral: Introduced in Senate
- 2026-05-18 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-18",
    "latestAction": {
      "actionDate": "2026-05-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4557",
    "number": "4557",
    "originChamber": "Senate",
    "policyArea": {},
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
    "title": "Outage Refund Protection Act",
    "type": "S",
    "updateDate": "2026-05-29T07:38:44Z",
    "updateDateIncludingText": "2026-05-29T07:38:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-18",
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
      "actionDate": "2026-05-18",
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
          "date": "2026-05-18T22:13:48Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4557is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4557\nIN THE SENATE OF THE UNITED STATES\nMay 18, 2026 Mr. Luj\u00e1n introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require telephone providers, cable television providers, direct broadcast satellite service providers, and internet providers to automatically refund their customers when their services are not working, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Outage Refund Protection Act .\n#### 2. Definitions\nIn this Act:\n**(1) Cable provider**\nThe term cable provider means a provider of cable service, as defined in section 3 of the Communications Act of 1934 ( 47 U.S.C. 153 ), with more than 5,000 customers.\n**(2) DBS provider**\nThe term DBS provider has the meaning given the term provider of direct broadcast satellite service in section 335 of the Communications Act of 1934 ( 47 U.S.C. 335 ) except that such provider shall have more than 5,000 customers.\n**(3) Internet provider**\nThe term internet provider means a provider of broadband internet access service, as defined in section 801 of the Communications Act of 1934 ( 47 U.S.C. 641 ), with more than 5,000 customers.\n**(4) Telephone provider**\nThe term telephone provider means\u2014\n**(A)**\na wireless carrier, as defined in section 7 of the Wireless Communications and Public Safety Act of 1999 ( 47 U.S.C. 615b ), with more than 5,000 customers;\n**(B)**\na wireline telephone service provider with more than 5,000 customers; and\n**(C)**\nan interconnected or non-interconnected VoIP service, as defined in section 3 of the Communications Act of 1934 ( 47 U.S.C. 153 ), with more than 5,000 customers.\n#### 3. Refunds\n##### (a) Cable services\n**(1) In general**\nA cable provider shall automatically credit the billing statement of a customer if\u2014\n**(A)**\nthe cable service of the cable provider is unavailable or is experiencing an outage or when the equipment provided to the customer by the cable provider to enable use of the cable service, including any software contained in or downloaded to the equipment is not operating correctly, for a period of 4 hours or more; or\n**(B)**\nthe customer terminates the cable service of the cable provider.\n**(2) Credits**\nIf required under paragraph (1), a credit shall be automatically issued to the customer for 1/30 of the monthly rate for each day the customer is not able to access the cable television network for a period of 4 hours or more.\n**(3) Refund**\n**(A) In general**\nIf a customer terminates cable service with a cable provider, any credit issued under this section that exceeds the amount due on a billing statement shall be issued to the customer not later than 30 days after the date of the outage in the form of a check in the customer's name, or by issuance of a no-fee prepaid debit card, or by electronic transfer, at the election of the customer, in the amount such credit exceeds such amount due.\n**(B) Exception**\nA cable provider shall not be required to issue a refund under subparagraph (A) if the amount of the refund exceeds the cost of disbursement under all methods permitted under this section. A cable provider may restrict the refund methods a customer can elect to the methods by which the amount of refund exceeds the cost of disbursement.\n##### (b) Satellite services\n**(1) In general**\nA DBS provider shall automatically credit the billing statement of a customer if\u2014\n**(A)**\nthe satellite service of the DBS provider is unavailable or is experiencing an outage or when the customer's satellite is not operating correctly, for a period of 4 hours or more; or\n**(B)**\nthe customer terminates the satellite service of the DBS provider.\n**(2) Credits**\nIf required under paragraph (1), a credit shall be automatically issued to the customer for 1/30 of the monthly rate for each day the customer is not able to access the satellite television network for a period of 4 hours or more.\n**(3) Refund**\n**(A) In general**\nIf a customer terminates satellite service with a DBS provider, any credit issued under this section that exceeds the amount due on a billing statement shall be issued to the customer not later than 30 days after the date of the outage in the form of a check in the customer's name, or by issuance of a no-fee prepaid debit card, or by electronic transfer, at the election of the customer, in the amount such credit exceeds such amount due.\n**(B) Exception**\nA DBS provider shall not be required to issue a refund under subparagraph (A) if the amount of the refund exceeds the cost of disbursement under all methods permitted under this section. A DBS provider may restrict the refund methods a customer can elect to the methods by which the amount of refund exceeds the cost of disbursement.\n##### (c) Internet services\n**(1) In general**\nAn internet provider shall automatically credit the billing statement of a customer if the broadband internet access service of the internet provider is out of service or is experiencing an outage, for a period of 4 hours or more.\n**(2) Credits**\nIf required under paragraph (1), a credit shall be automatically issued for 1/30 of the monthly rate for each day the broadband internet access service is unavailable for a period of 4 hours or more.\n**(3) Refund**\n**(A) In general**\nIf a customer terminates broadband internet access service with an internet provider, any credit issued under this section that exceeds the amount due on a billing statement shall be issued to the customer not later than 30 days after the date of the outage in the form of a check in the customer's name, or by issuance of a no-fee prepaid debit card, or by electronic transfer, at the election of the customer, in the amount such credit exceeds such amount due.\n**(B) Exception**\nAn internet provider shall not be required to issue a refund under subparagraph (A) if the amount of the refund exceeds the cost of disbursement under all methods permitted under this section. An internet provider may restrict the refund methods a customer can elect to the methods by which the amount of refund exceeds the cost of disbursement.\n##### (d) Telephone services\n**(1) In general**\nA telephone provider shall automatically credit the billing statement of a customer on a per-line basis if the telephone service of the telephone provider is out of service or is experiencing an outage, for a period of 4 hours or more.\n**(2) Credits**\nIf required under paragraph (1), a credit shall be automatically issued for 1/30 of the monthly rate for each day the customer is not able to access telephone service of the telephone provider for a period of 4 hours or more.\n**(3) Refund**\n**(A) In general**\nIf a customer terminates telephone service with a telephone provider, any credit issued under this section that exceeds the amount due on a billing statement shall be issued to the customer not later than 30 days after the date of the outage in the form of a check in the customer's name, or by issuance of a no-fee prepaid debit card, or by electronic transfer, at the election of the customer, in the amount such credit exceeds such amount due.\n**(B) Exception**\nA telephone provider shall not be required to issue a refund under subparagraph (A) if the amount of the refund exceeds the cost of disbursement under all methods permitted under this section. A telephone provider may restrict the refund methods a customer can elect to the methods by which the amount of refund exceeds the cost of disbursement.\n##### (e) Pre-Planned maintenance\nSubsections (a) through (d) shall not apply to service outages for pre-planned maintenance for which the provider has informed the affected customers in advance that service will be unavailable.\n##### (f) Enforcement\nNot later than 18 months after the date of enactment of this Act, the Federal Communications Commission shall issue rules implementing the requirements under this section, including penalties for failure to comply.\n##### (g) Preemption\nNothing in this section or in the regulations prescribed under this section shall preempt any State law that imposes more restrictive intrastate requirements or regulations.\n#### 4. Customer service improvements\n##### (a) In general\n**(1) Federal Communications Commission**\nNot later than 18 months after the date of enactment of this Act, the Federal Communications Commission shall issue rules to require that each telephone provider, cable provider, DBS provider, and internet provider\u2014\n**(A)**\nextend cable customer service requirements to direct broadcast satellite, voice, and broadband service, as applicable, including by making customer service accessible for those with disabilities;\n**(B)**\nmaintain recordings of customer service calls for not less than 1 year and release a recording of a customer service call to a customer or the customer's agent, upon request; and\n**(C)**\nnot associate any fee with the option to receive a call from a customer service representative at such time as a representative becomes available.\n**(2) Federal Trade Commission**\n**(A) In general**\nNot later than 18 months after the date of enactment of this Act, the Federal Trade Commission shall issue rules with respect to telephone providers, cable providers, DBS providers, and internet providers to\u2014\n**(i)**\nimplement standards for missed service appointments; and\n**(ii)**\nassess the burden of returning equipment for those with disabilities or individuals who do not drive and if, in the determination of the Federal Trade Commission, the burden is sufficiently high, require the provider to offer alternate means of return at no extra cost to such individuals.\n**(B) Injunction authority**\nThe Federal Trade Commission shall have authority under section 13(b) of the Federal Trade Commission Act ( 15 U.S.C. 53(b) ) to seek a preliminary or permanent injunctions to enforce any requirement under subparagraph (A).\n##### (b) Rule of construction\nNothing in this section shall prohibit a State, or subdivision of a State, from imposing requirements higher than or in addition to the requirements imposed pursuant to this section.\n#### 5. Service outages\nAs soon as possible following the activation of the Disaster Information Reporting System described in section 4.18 of title 47, Code of Federal Regulations, or any successor regulation, each broadband internet service provider shall report service outages within the area of activation to the Federal Communications Commission and shall include broadband internet access service outage information in each public report under the Disaster Information Reporting System.",
      "versionDate": "2026-05-18",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4557is.xml"
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
      "title": "Outage Refund Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-29T07:38:44Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Outage Refund Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-29T07:38:43Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require telephone providers, cable television providers, direct broadcast satellite service providers, and internet providers to automatically refund their customers when their services are not working, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-29T07:33:50Z"
    }
  ]
}
```
