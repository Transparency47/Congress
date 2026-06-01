# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/281?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/281
- Title: TICKET Act
- Congress: 119
- Bill type: S
- Bill number: 281
- Origin chamber: Senate
- Introduced date: 2025-01-28
- Update date: 2025-10-09T03:26:24Z
- Update date including text: 2025-10-09T03:26:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in Senate
- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-02-05 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably.
- 2025-04-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-17.
- 2025-04-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-17.
- 2025-04-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 63.
- Latest action: 2025-01-28: Introduced in Senate

## Actions

- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-02-05 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably.
- 2025-04-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-17.
- 2025-04-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-17.
- 2025-04-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 63.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/281",
    "number": "281",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "TICKET Act",
    "type": "S",
    "updateDate": "2025-10-09T03:26:24Z",
    "updateDateIncludingText": "2025-10-09T03:26:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 63.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-17.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-17.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
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
            "date": "2025-04-29T18:49:19Z",
            "name": "Reported By"
          },
          {
            "date": "2025-02-05T15:00:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-28T20:47:24Z",
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
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s281is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 281\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2025 Mr. Schmitt (for himself and Mr. Markey ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require sellers of event tickets to disclose comprehensive information to consumers about ticket prices and related fees, to prohibit speculative ticketing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transparency In Charges for Key Events Ticketing Act or the TICKET Act .\n#### 2. All inclusive ticket price disclosure\nBeginning 180 days after the date of the enactment of this Act, it shall be unlawful for a ticket issuer, secondary market ticket issuer, or secondary market ticket exchange to offer for sale an event ticket unless the ticket issuer, secondary market ticket issuer, or secondary market ticket exchange\u2014\n**(1)**\nclearly and conspicuously displays the total event ticket price, if a price is displayed, in any advertisement, marketing, or price list wherever the ticket is offered for sale;\n**(2)**\nclearly and conspicuously discloses to any individual who seeks to purchase an event ticket the total event ticket price at the time the ticket is first displayed to the individual and anytime thereafter throughout the ticket purchasing process; and\n**(3)**\nprovides an itemized list of the base event ticket price and each event ticket fee prior to the completion of the ticket purchasing process.\n#### 3. Speculative ticketing ban\n##### (a) Prohibition\nBeginning 180 days after the date of the enactment of this Act, a ticket issuer, secondary market ticket issuer, or secondary market ticket exchange that does not have actual or constructive possession of an event ticket shall not sell, offer for sale, or advertise for sale such event ticket.\n##### (b) Services permitted\nNotwithstanding subsection (a), a secondary market ticket issuer or secondary market ticket exchange may sell, offer for sale, or advertise for sale a service to an individual to obtain an event ticket on behalf of such individual if the secondary market ticket issuer or secondary market ticket exchange complies with the following:\n**(1)**\nDoes not market or list the service as an event ticket.\n**(2)**\nMaintains a clear, distinct, and easily discernible separation between the service and event tickets that persists throughout the entire service selection and purchasing process.\n**(3)**\nClearly and conspicuously discloses before selection of the service that the service is not an event ticket and that the purchase of the service does not guarantee an event ticket.\n#### 4. Disclosures\nA ticket issuer, secondary market ticket issuer, or secondary market ticket exchange\u2014\n**(1)**\nif offering an event ticket for resale, shall provide a clear and conspicuous statement, before a consumer purchases the event ticket from the ticket issuer, secondary market ticket issuer, or secondary market ticket exchange, that the issuer or exchange is engaged in the secondary sale of event tickets; and\n**(2)**\nshall not state that the ticket issuer, secondary market ticket issuer, or secondary market ticket exchange is affiliated with or endorsed by a venue, team, or artist, as applicable, including by using words like official in promotional materials, social media promotions, or paid advertising, unless a partnership agreement has been executed or the issuer or exchange has the express written consent of the venue, team, or artist, as applicable.\n#### 5. Refund requirements\n##### (a) Cancellation\nBeginning 180 days after the date of the enactment of this Act, if an event is canceled or postponed (except for a case in which an event is canceled or postponed due to a cause beyond the reasonable control of the issuer, including a natural disaster, civil disturbance, or otherwise unforeseeable impediment), a ticket issuer, secondary market ticket issuer, or secondary market ticket exchange shall provide the purchaser of an event ticket from the issuer or exchange for the canceled or postponed event, at a minimum\u2014\n**(1)**\nif the event is cancelled, a full refund for the total event ticket price;\n**(2)**\nsubject to availability, if the event is postponed for not more than 6 months and the original event ticket is no longer valid for entry to the rescheduled event, a replacement event ticket for the rescheduled event in the same or a comparable location once the event has been rescheduled; or\n**(3)**\nif the event is postponed for more than 6 months, at the option of the purchaser\u2014\n**(A)**\na full refund for the total event ticket price; or\n**(B)**\nif the original event ticket is no longer valid for entry to the rescheduled event, a replacement event ticket for the rescheduled event in the same or a comparable location once the event has been rescheduled.\n##### (b) Disclosure of guarantee and refund policy required\nBeginning 180 days after the date of the enactment of this Act, a ticket issuer, secondary market ticket issuer, or secondary market ticket exchange shall disclose clearly and conspicuously to a purchaser before the completion of an event ticket sale the guarantee or refund policy of such ticket issuer, secondary market ticket issuer, or secondary market ticket exchange, including under what circumstances any refund issued will include a refund of any event ticket fee.\n##### (c) Disclosure of how To obtain a refund required\nBeginning 180 days after the date of the enactment of this Act, a ticket issuer, secondary market ticket issuer, or secondary market ticket exchange shall provide a clear and conspicuous explanation of how to obtain a refund of the total event ticket price.\n#### 6. Report by the Federal Trade Commission on BOTS Act of 2016 enforcement\nNot later than 6 months after the date of the enactment of this Act, the Commission shall submit to Congress a report on enforcement of the Better Online Ticket Sales Act of 2016 ( Public Law 114\u2013274 ; 15 U.S.C. 45c ), including any enforcement action taken, challenges with enforcement and coordination with State Attorneys General, and recommendations on how to improve enforcement and industry compliance.\n#### 7. Enforcement\n##### (a) Unfair or deceptive act or practice\nA violation of this Act shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n##### (b) Powers of commission\n**(1) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(2) Privileges and immunities**\nAny person who violates this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n#### 8. Definitions\nIn this Act:\n**(1) Artist**\nThe term artist means any performer, musician, comedian, producer, ensemble or production entity of a theatrical production, sports team owner, or similar person.\n**(2) Base event ticket price**\nThe term base event ticket price means, with respect to an event ticket, the price of the event ticket excluding the cost of any event ticket fees.\n**(3) Commission**\nThe term Commission means the Federal Trade Commission.\n**(4) Event**\nThe term event means any live concert, theatrical performance, sporting event, show, or similarly scheduled live activity, that is\u2014\n**(A)**\ntaking place in a venue with a seating or attendance capacity exceeding 200 persons;\n**(B)**\nopen to the general public; and\n**(C)**\npromoted, advertised, or marketed in interstate commerce, or for which event tickets are generally sold or distributed in interstate commerce.\n**(5) Event ticket; ticket issuer**\nThe terms event ticket and ticket issuer have the meaning given those terms in the Better Online Ticket Sales Act of 2016 ( Public Law 114\u2013274 ).\n**(6) Event ticket fee**\nThe term event ticket fee \u2014\n**(A)**\nmeans a charge for an event ticket that must be paid in addition to the base event ticket price in order to obtain an event ticket from a ticket issuer, secondary market ticket issuer, or secondary market ticket exchange, including any service fee, charge and order processing fee, delivery fee, facility charge fee, tax, and any other charge; and\n**(B)**\ndoes not include any charge or fee for an optional product or service associated with the event that may be selected by a purchaser of an event ticket.\n**(7) Optional product or service**\nThe term optional product or service means a product or service that an individual does not need to purchase to use or take possession of an event ticket.\n**(8) Resale; secondary sale**\nThe terms resale and secondary sale mean any sale of an event ticket that occurs after the initial sale of the event ticket by a ticket issuer.\n**(9) Secondary market ticket exchange**\nThe term secondary market ticket exchange means any person that in the regular course of trade or business of that person operates a platform or exchange for advertising, listing, or selling resale tickets, on behalf of itself, vendors, or a secondary market ticket issuer.\n**(10) Secondary market ticket issuer**\nThe term secondary market ticket issuer means any person, including a ticket issuer, that resells or makes a secondary sale of an event ticket to the general public in the regular course of the trade or business of the person.\n**(11) Total event ticket price**\nThe term total event ticket price means, with respect to an event ticket, the total cost of the event ticket, including the base event ticket price and any event ticket fee.\n**(12) Venue**\nThe term venue means a physical space at which an event takes place.",
      "versionDate": "2025-01-28",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s281rs.xml",
      "text": "II\nCalendar No. 63\n119th CONGRESS\n1st Session\nS. 281\n[Report No. 119\u201317]\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2025 Mr. Schmitt (for himself and Mr. Markey ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nApril 29, 2025 Reported by Mr. Cruz , with amendments Omit the part struck through and insert the parts printed in italic\nA BILL\nTo require sellers of event tickets to disclose comprehensive information to consumers about ticket prices and related fees, to prohibit speculative ticketing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transparency In Charges for Key Events Ticketing Act or the TICKET Act .\n#### 2. All inclusive ticket price disclosure\nBeginning 180 days after the date of the enactment of this Act, it shall be unlawful for a ticket issuer, secondary market ticket issuer, or secondary market ticket exchange to offer for sale an event ticket unless the ticket issuer, secondary market ticket issuer, or secondary market ticket exchange\u2014\n**(1)**\nclearly and conspicuously displays the total event ticket price, if a price is displayed, in any advertisement, marketing, or price list wherever the ticket is offered for sale;\n**(2)**\nclearly and conspicuously discloses to any individual who seeks to purchase an event ticket the total event ticket price at the time the ticket is first displayed to the individual and anytime thereafter throughout the ticket purchasing process; and\n**(3)**\nprovides an itemized list of the base event ticket price and each event ticket fee prior to the completion of the ticket purchasing process.\n#### 3. Speculative ticketing ban\n##### (a) Prohibition\nBeginning 180 days after the date of the enactment of this Act, a ticket issuer, secondary market ticket issuer, or secondary market ticket exchange that does not have actual or constructive possession of an event ticket shall not sell, offer for sale, or advertise for sale such event ticket.\n##### (b) Services permitted\nNotwithstanding subsection (a), a secondary market ticket issuer or secondary market ticket exchange may sell, offer for sale, or advertise for sale a service to an individual to obtain an event ticket on behalf of such individual if the secondary market ticket issuer or secondary market ticket exchange complies with the following:\n**(1)**\nDoes not market or list the service as an event ticket.\n**(2)**\nMaintains a clear, distinct, and easily discernible separation between the service and event tickets that persists throughout the entire service selection and purchasing process.\n**(3)**\nClearly and conspicuously discloses before selection of the service that the service is not an event ticket and that the purchase of the service does not guarantee an event ticket.\n#### 4. Disclosures\nA ticket issuer, secondary market ticket issuer, or secondary market ticket exchange\u2014\n**(1)**\nif offering an event ticket for resale, shall provide a clear and conspicuous statement, before a consumer purchases the event ticket from the ticket issuer, secondary market ticket issuer, or secondary market ticket exchange, that the issuer or exchange is engaged in the secondary sale of event tickets; and\n**(2)**\nshall not state that the ticket issuer, secondary market ticket issuer, or secondary market ticket exchange is affiliated with or endorsed by a venue, team, or artist, as applicable, including by using words like official in promotional materials, social media promotions, or paid advertising, unless a partnership agreement has been executed or the issuer or exchange has the express written consent of the venue, team, or artist, as applicable . ; and\n**(3)**\nshall not include the name of the venue, including any misspellings of any such name, in a domain name, or any subdomain thereof, in the URL of the secondary market ticket issuer or secondary market ticket exchange unless authorized by the owner of the venue.\n#### 5. Refund requirements\n##### (a) Cancellation\nBeginning 180 days after the date of the enactment of this Act, if an event is canceled or postponed (except for a case in which an event is canceled or postponed due to a cause beyond the reasonable control of the issuer, including a natural disaster, civil disturbance, or otherwise unforeseeable impediment), a ticket issuer, secondary market ticket issuer, or secondary market ticket exchange shall provide the purchaser of an event ticket from the issuer or exchange for the canceled or postponed event, at a minimum\u2014\n**(1)**\nif the event is cancelled, a full refund for the total event ticket price;\n**(2)**\nsubject to availability, if the event is postponed for not more than 6 months and the original event ticket is no longer valid for entry to the rescheduled event, a replacement event ticket for the rescheduled event in the same or a comparable location once the event has been rescheduled; or\n**(3)**\nif the event is postponed for more than 6 months, at the option of the purchaser\u2014\n**(A)**\na full refund for the total event ticket price; or\n**(B)**\nif the original event ticket is no longer valid for entry to the rescheduled event, a replacement event ticket for the rescheduled event in the same or a comparable location once the event has been rescheduled.\n##### (b) Disclosure of guarantee and refund policy required\nBeginning 180 days after the date of the enactment of this Act, a ticket issuer, secondary market ticket issuer, or secondary market ticket exchange shall disclose clearly and conspicuously to a purchaser before the completion of an event ticket sale the guarantee or refund policy of such ticket issuer, secondary market ticket issuer, or secondary market ticket exchange, including under what circumstances any refund issued will include a refund of any event ticket fee.\n##### (c) Disclosure of how To obtain a refund required\nBeginning 180 days after the date of the enactment of this Act, a ticket issuer, secondary market ticket issuer, or secondary market ticket exchange shall provide a clear and conspicuous explanation of how to obtain a refund of the total event ticket price.\n#### 6. Report by the Federal Trade Commission on BOTS Act of 2016 enforcement\nNot later than 6 months after the date of the enactment of this Act, the Commission shall submit to Congress a report on enforcement of the Better Online Ticket Sales Act of 2016 ( Public Law 114\u2013274 ; 15 U.S.C. 45c ), including any enforcement action taken, challenges with enforcement and coordination with State Attorneys General, and recommendations on how to improve enforcement and industry compliance.\n#### 7. Enforcement\n##### (a) Unfair or deceptive act or practice\nA violation of this Act shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n##### (b) Powers of commission\n**(1) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(2) Privileges and immunities**\nAny person who violates this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n#### 8. Definitions\nIn this Act:\n**(1) Artist**\nThe term artist means any performer, musician, comedian, producer, ensemble or production entity of a theatrical production, sports team owner, or similar person.\n**(2) Base event ticket price**\nThe term base event ticket price means, with respect to an event ticket, the price of the event ticket excluding the cost of any event ticket fees.\n**(3) Commission**\nThe term Commission means the Federal Trade Commission.\n**(4) Event**\nThe term event means any live concert, theatrical performance, sporting event, show, or similarly scheduled live activity, that is\u2014\n**(A)**\ntaking place in a venue with a seating or attendance capacity exceeding 200 persons;\n**(B)**\nopen to the general public; and\n**(C)**\npromoted, advertised, or marketed in interstate commerce, or for which event tickets are generally sold or distributed in interstate commerce.\n**(5) Event ticket; ticket issuer**\nThe terms event ticket and ticket issuer have the meaning given those terms in the Better Online Ticket Sales Act of 2016 ( Public Law 114\u2013274 ).\n**(6) Event ticket fee**\nThe term event ticket fee \u2014\n**(A)**\nmeans a charge for an event ticket that must be paid in addition to the base event ticket price in order to obtain an event ticket from a ticket issuer, secondary market ticket issuer, or secondary market ticket exchange, including any service fee, charge and order processing fee, delivery fee, facility charge fee, tax, and any other charge; and\n**(B)**\ndoes not include any charge or fee for an optional product or service associated with the event that may be selected by a purchaser of an event ticket.\n**(7) Optional product or service**\nThe term optional product or service means a product or service that an individual does not need to purchase to use or take possession of an event ticket.\n**(8) Resale; secondary sale**\nThe terms resale and secondary sale mean any sale of an event ticket that occurs after the initial sale of the event ticket by a ticket issuer.\n**(9) Secondary market ticket exchange**\nThe term secondary market ticket exchange means any person that in the regular course of trade or business of that person operates a platform or exchange for advertising, listing, or selling resale tickets, on behalf of itself, vendors, or a secondary market ticket issuer.\n**(10) Secondary market ticket issuer**\nThe term secondary market ticket issuer means any person, including a ticket issuer, that resells or makes a secondary sale of an event ticket to the general public in the regular course of the trade or business of the person.\n**(11) Total event ticket price**\nThe term total event ticket price means, with respect to an event ticket, the total cost of the event ticket, including the base event ticket price and any event ticket fee.\n**(12) URL**\nThe term URL means the uniform resource locator associated with an internet website.\n**(13) Venue**\nThe term venue means a physical space at which an event takes place.",
      "versionDate": "2025-04-29",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-09-16",
        "text": "Read twice. Placed on Senate Legislative Calendar under General Orders. Calendar No. 163."
      },
      "number": "1402",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "TICKET Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Competition and antitrust",
            "updateDate": "2025-02-20T14:46:24Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-02-20T14:46:24Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-02-20T14:46:24Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2025-02-20T14:46:24Z"
          },
          {
            "name": "Service industries",
            "updateDate": "2025-02-20T14:46:24Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-02-20T14:46:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-02-18T14:34:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s281",
          "measure-number": "281",
          "measure-type": "s",
          "orig-publish-date": "2025-01-28",
          "originChamber": "SENATE",
          "update-date": "2025-09-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s281v00",
            "update-date": "2025-09-10"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Transparency In Charges for Key Events Ticketing Act or the TICKET Act</strong></p><p>This bill requires ticket sellers (including sellers on the secondary market) for concerts, performances, sporting events, and similar activities to clearly and prominently disclose the total ticket price for the event\u00a0at the time the ticket is first displayed to an individual (and anytime thereafter during the purchasing process). Prior to completing a purchase, ticket sellers also must provide an itemized list of the base ticket price and each fee (e.g., service fee, processing fee, or other charge). The total ticket price must also be disclosed in any advertisement, marketing, or price list.</p><p>Additionally, a ticket seller, secondary market seller, or ticket exchange that does not have actual or constructive possession of an event ticket is prohibited from selling or advertising a ticket for the event. However, a secondary market seller or exchange may sell or advertise a service to obtain an event ticket for an individual\u00a0if the seller or exchange (1) does not market the service as an event ticket, (2) maintains a clear separation between the provided service and the event tickets throughout the entire purchasing process, and (3) clearly discloses that the service is not an event ticket.</p><p>The bill establishes additional disclosure requirements for\u00a0ticket sellers, secondary market sellers, and ticket exchanges, and requires such entities to issue a refund for the total ticket price if an event is canceled or postponed.</p><p>The Federal Trade Commission must enforce these requirements.</p>"
        },
        "title": "TICKET Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s281.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Transparency In Charges for Key Events Ticketing Act or the TICKET Act</strong></p><p>This bill requires ticket sellers (including sellers on the secondary market) for concerts, performances, sporting events, and similar activities to clearly and prominently disclose the total ticket price for the event\u00a0at the time the ticket is first displayed to an individual (and anytime thereafter during the purchasing process). Prior to completing a purchase, ticket sellers also must provide an itemized list of the base ticket price and each fee (e.g., service fee, processing fee, or other charge). The total ticket price must also be disclosed in any advertisement, marketing, or price list.</p><p>Additionally, a ticket seller, secondary market seller, or ticket exchange that does not have actual or constructive possession of an event ticket is prohibited from selling or advertising a ticket for the event. However, a secondary market seller or exchange may sell or advertise a service to obtain an event ticket for an individual\u00a0if the seller or exchange (1) does not market the service as an event ticket, (2) maintains a clear separation between the provided service and the event tickets throughout the entire purchasing process, and (3) clearly discloses that the service is not an event ticket.</p><p>The bill establishes additional disclosure requirements for\u00a0ticket sellers, secondary market sellers, and ticket exchanges, and requires such entities to issue a refund for the total ticket price if an event is canceled or postponed.</p><p>The Federal Trade Commission must enforce these requirements.</p>",
      "updateDate": "2025-09-10",
      "versionCode": "id119s281"
    },
    "title": "TICKET Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Transparency In Charges for Key Events Ticketing Act or the TICKET Act</strong></p><p>This bill requires ticket sellers (including sellers on the secondary market) for concerts, performances, sporting events, and similar activities to clearly and prominently disclose the total ticket price for the event\u00a0at the time the ticket is first displayed to an individual (and anytime thereafter during the purchasing process). Prior to completing a purchase, ticket sellers also must provide an itemized list of the base ticket price and each fee (e.g., service fee, processing fee, or other charge). The total ticket price must also be disclosed in any advertisement, marketing, or price list.</p><p>Additionally, a ticket seller, secondary market seller, or ticket exchange that does not have actual or constructive possession of an event ticket is prohibited from selling or advertising a ticket for the event. However, a secondary market seller or exchange may sell or advertise a service to obtain an event ticket for an individual\u00a0if the seller or exchange (1) does not market the service as an event ticket, (2) maintains a clear separation between the provided service and the event tickets throughout the entire purchasing process, and (3) clearly discloses that the service is not an event ticket.</p><p>The bill establishes additional disclosure requirements for\u00a0ticket sellers, secondary market sellers, and ticket exchanges, and requires such entities to issue a refund for the total ticket price if an event is canceled or postponed.</p><p>The Federal Trade Commission must enforce these requirements.</p>",
      "updateDate": "2025-09-10",
      "versionCode": "id119s281"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s281is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s281rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "TICKET Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-01T11:48:16Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "TICKET Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-05-01T02:23:15Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Transparency In Charges for Key Events Ticketing Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-05-01T02:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TICKET Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T15:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Transparency In Charges for Key Events Ticketing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T15:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require sellers of event tickets to disclose comprehensive information to consumers about ticket prices and related fees, to prohibit speculative ticketing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T15:18:24Z"
    }
  ]
}
```
