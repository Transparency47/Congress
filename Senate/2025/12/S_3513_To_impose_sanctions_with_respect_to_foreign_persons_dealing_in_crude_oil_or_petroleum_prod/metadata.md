# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3513?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3513
- Title: Decreasing Russian Oil Profits Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3513
- Origin chamber: Senate
- Introduced date: 2025-12-16
- Update date: 2026-03-03T12:03:27Z
- Update date including text: 2026-03-03T12:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in Senate
- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-12-16: Introduced in Senate

## Actions

- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3513",
    "number": "3513",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001243",
        "district": "",
        "firstName": "David",
        "fullName": "Sen. McCormick, David [R-PA]",
        "lastName": "McCormick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Decreasing Russian Oil Profits Act of 2025",
    "type": "S",
    "updateDate": "2026-03-03T12:03:27Z",
    "updateDateIncludingText": "2026-03-03T12:03:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-16",
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
            "date": "2025-12-16T22:45:24Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-16T22:45:24Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MA"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "OH"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "DE"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "UT"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3513is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3513\nIN THE SENATE OF THE UNITED STATES\nDecember 16, 2025 Mr. McCormick (for himself, Ms. Warren , Mr. Husted , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo impose sanctions with respect to foreign persons dealing in crude oil or petroleum products of Russian Federation origin.\n#### 1. Short title\nThis Act may be cited as the Decreasing Russian Oil Profits Act of 2025 .\n#### 2. Imposition of sanctions with respect to trade in Russian origin petroleum products\n##### (a) In general\nBeginning on the date that is 90 days after the date of the enactment of this Act, the President shall impose the sanctions described in subsection (b) with respect to any foreign person that the Secretary of the Treasury, in consultation with the Secretary of State, determines\u2014\n**(1)**\nis responsible for or complicit in, or has directly or indirectly engaged or attempted to engage in, the purchase or importation into any country of crude oil or petroleum products of Russian Federation origin;\n**(2)**\nhas knowingly facilitated financial transactions related to an activity described in paragraph (1);\n**(3)**\nhas materially assisted, sponsored, or provided material support for any activity described in paragraph (1) or (2) by any person with respect to which sanctions have been imposed under paragraph (1) or (2); or\n**(4)**\nis or has been a chief executive officer or member of the board of directors of any entity described in any of paragraphs (1) through (3).\n##### (b) Sanctions described\nThe sanctions described in this subsection are the exercise all of the powers granted to the President by the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in property and interests in property of a foreign person if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n##### (c) Permissible exception frameworks\n**(1) In general**\nThe President may apply not more than 2 of the types of exceptions described in paragraph (2) with respect to the application of sanctions under subsection (a).\n**(2) Exceptions described**\n**(A) Exception for countries that isolate Russian funds and reduce purchases**\n**(i) In general**\nThe President may apply an exception to the application of sanctions under subsection (a) with respect to the purchase or importation into a country of crude oil or petroleum products of Russian Federation origin if the President determines and certifies in writing to the appropriate congressional committees that\u2014\n**(I)**\nany funds owed by the government of that country or persons of that country to the Russian Federation or to the sellers of crude oil or petroleum products of Russian Federation origin as a result of the purchase or importation will be\u2014\n**(aa)**\ncredited to an account located in that country; and\n**(bb)**\nused only to facilitate transactions in agricultural commodities, food, medicine, or medical devices between the Russian Federation and the country; and\n**(II)**\nthe government of the country has committed to significantly reduce its purchases of crude oil and petroleum products of Russian Federation origin.\n**(ii) Renewal required**\nThe authority to apply the exception under clause (i) shall expire if the President does not certify, not later than 180 days after the date of the enactment of this Act, and every 180 days thereafter, that\u2014\n**(I)**\nthe country has significantly reduced its volume of purchases of crude oil and petroleum products of Russian Federation origin during the preceding 180-day period; or\n**(II)**\nthe price and supply of crude oil and petroleum products produced in countries other than the Russian Federation is not sufficient to permit purchasers of crude oil and petroleum products of Russian Federation origin to reduce significantly in volume their purchases from the Russian Federation.\n**(iii) Sanctions for misuse of account**\nAny foreign person responsible for or complicit in, or that has directly or indirectly engaged or attempted to engage in, transactions reliant on the funds in an account described in clause (i)(I) for any purpose other than to facilitate transactions in agricultural commodities, food, medicine, or medical devices between the Russian Federation and the country in which the account is located shall be subject to the sanctions described in subsection (b).\n**(B) Exception for deposits into account to support Ukraine**\n**(i) In general**\nThe President may apply an exception to the application of sanctions under subsection (a) with respect to the purchase or importation into a country of crude oil or petroleum products of Russian Federation origin if a payment per barrel of such crude oil or petroleum products has been deposited into an account that the President has established for the benefit of Ukraine.\n**(ii) Guidance**\nThe President may issue guidance and develop implementation tools that assist private sector entities in verifying that the payments described in clause (i) corresponding to specific purchases have been deposited in the account described in that clause.\n**(iii) Use of funds**\n**(I) In general**\nThe funds in an account established as described in clause (i) shall be available only for\u2014\n**(aa)**\nthe purposes specified in section 104(f) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note); and\n**(bb)**\nfunding the purchase by the Government of Ukraine of defense articles for Ukraine to employ in response to Russian Federation aggression.\n**(II) Timely disbursement**\nA significant proportion of funds in an account established as described in clause (i) shall be disbursed not less frequently than every 90 days for the purposes described in subclause (I).\n**(iv) Limitations on transfers and expenditures of funds**\n**(I) Notification of transfers**\n**(aa) In general**\nThe Secretary of State shall notify the appropriate congressional committees not fewer than 15 days before transferring any funds from an account established as described in clause (i) to any other account for the purposes described in clause (iii) or otherwise expending any of such funds for such purposes.\n**(bb) Elements**\nA notification under item (aa) shall specify\u2014\n(AA)\nthe amount of funds to be transferred or expended;\n(BB)\nthe specific purpose for which the funds are transferred or expended; and\n(CC)\nthe recipient of those funds.\n**(II) Certification of transparency and accountability**\nNo funds may be transferred or otherwise expended from an account established as described in clause (i) unless the President submits to the appropriate congressional committees in writing a certification that a plan exists to ensure transparency and accountability for all funds transferred into and expended from any account receiving the funds.\n**(III) Joint resolution of disapproval**\nNo funds may be transferred or expended pursuant to this clause if, within 15 days of receipt of the notification under subclause (I), a joint resolution is enacted into law prohibiting such transfer.\n**(C) Exception for countries supporting Ukraine**\n**(i) In general**\nThe President may apply an exception to the application of sanctions under subsection (a) with respect to the purchase or importation into any country of crude oil or petroleum products of Russian Federation origin if the President determines and certifies in writing to the appropriate congressional committees that the government of that country is providing significant economic or military support to the Government of Ukraine.\n**(ii) Renewal required**\nThe authority to apply the exception under clause (i) with respect to a country shall expire if the President does not certify, not later than 180 days after the date of the enactment of this Act, and every 180 days thereafter, that the government of the country is providing significant economic or military support to the Government of Ukraine.\n**(D) Temporary port-specific exceptions**\n**(i) In general**\nDuring the period beginning on the date of the enactment of this Act and ending on the date that is 270 days after such date of enactment, the President may apply an exception to the application of sanctions under subsection (a) for the purchase or the importation into any country of crude oil or petroleum products of Russian Federation exported from specific Russian Federation ports if the President submits to the appropriate congressional committees a report providing a justification for the exception.\n**(ii) Limitation**\nAn exception applied under clause (i) may not cover, at any time, ports that are estimated to have cumulatively accounted for more than half of the oil export capacity of the Russian Federation in 2024.\n**(3) Sanctions related to crude oil and petroleum products sold above price cap without regard to Group of 7 nexus**\n**(A) In general**\nAny exception described in paragraph (2) that the President applies to the requirement to impose sanctions under subsection (a) shall not apply with respect to an activity described in subparagraph (B) if the activity facilitates the maritime transport of crude oil or petroleum products of Russian Federation origin purchased for an amount greater than the relevant price cap determined by the Secretary of the Treasury for crude oil or petroleum products of Russian Federation origin.\n**(B) Activities described**\nThe activities described in this subparagraph are transporting, trading or commodities brokering, financing, shipping, insuring, flagging, or customs brokering related to the purchase or importation of crude oil or petroleum products of Russian Federation origin.\n**(C) Applicability to service providers based outside of group of 7 countries**\nSubparagraph (A) applies without regard to whether the person engaging in an activity described in subparagraph (B) is organized under the laws of or otherwise subject to the jurisdiction of a country that is a member of the Group of 7.\n##### (d) Sunset\nThe provisions of this section, and any sanctions imposed under this section, shall terminate on the date that is 5 years after the date of the enactment of this Act.\n##### (e) Definitions\nIn this section:\n**(1) Agricultural commodity**\nThe term agricultural commodity has the meaning given such term in section 102 of the Agricultural Trade Act of 1978 ( 7 U.S.C. 5602 ).\n**(2) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Banking, Housing, and Urban Affairs and the Committee on Foreign Relations of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs and the Committee on Financial Services of the House of Representatives.\n**(3) Defense article**\nThe term defense article has the meaning given that term in section 47 of the Arms Export Control Act ( 22 U.S.C. 2794 ).\n**(4) Foreign person**\nThe term foreign person means an individual or entity that is not a United States person.\n**(5) Knowingly**\nThe term knowingly , with respect to conduct, a circumstance, or a result, means that a person had actual knowledge, or should have known, of the conduct, the circumstance, or the result.\n**(6) Medical device**\nThe term medical device has the meaning given the term device in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ).\n**(7) Medicine**\nThe term medicine has the meaning given the term drug in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ).\n**(8) United states person**\nThe term United States person means\u2014\n**(A)**\na United States citizen or an alien lawfully admitted for permanent residence to the United States;\n**(B)**\nan entity organized under the laws of the United States or any jurisdiction within the United States, including a foreign branch of such an entity; or\n**(C)**\nany person located in the United States.",
      "versionDate": "2025-12-16",
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
        "actionDate": "2026-02-11",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "7506",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Decreasing Russian Oil Profits Act of 2026",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-01-12T22:38:06Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3513is.xml"
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
      "title": "Decreasing Russian Oil Profits Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T12:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Decreasing Russian Oil Profits Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-10T09:09:05Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to impose sanctions with respect to foreign persons dealing in crude oil or petroleum products of Russian Federation origin.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-10T09:03:25Z"
    }
  ]
}
```
