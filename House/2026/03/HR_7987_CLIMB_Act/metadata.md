# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7987?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7987
- Title: CLIMB Act
- Congress: 119
- Bill type: HR
- Bill number: 7987
- Origin chamber: House
- Introduced date: 2026-03-18
- Update date: 2026-05-13T08:06:51Z
- Update date including text: 2026-05-13T08:06:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-18: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-03-18: Introduced in House

## Actions

- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-18",
    "latestAction": {
      "actionDate": "2026-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7987",
    "number": "7987",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "R000610",
        "district": "14",
        "firstName": "Guy",
        "fullName": "Rep. Reschenthaler, Guy [R-PA-14]",
        "lastName": "Reschenthaler",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "CLIMB Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:51Z",
    "updateDateIncludingText": "2026-05-13T08:06:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-18",
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
          "date": "2026-03-18T14:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "LA"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7987ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7987\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2026 Mr. Reschenthaler (for himself and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo prohibit Federal agencies from taking any adverse action against a person solely because the person provides business assistance to a cannabis-related legitimate business, to amend the Securities Exchange Act of 1934 to create a safe harbor for national securities exchanges to list the securities of issuers that are cannabis-related legitimate businesses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Capital Lending and Investment for Marijuana Businesses Act or the CLIMB Act .\n#### 2. Prohibition on Federal agencies taking certain actions against persons who provide business assistance to cannabis-related legitimate businesses\n##### (a) In general\nA Federal agency may not take any adverse action against a person solely because the person provides business assistance to a cannabis-related legitimate business or service provider.\n##### (b) Definitions\nIn this section:\n**(1) Business assistance**\nThe term business assistance means\u2014\n**(A)**\nproviding a financial product or service;\n**(B)**\nselling insurance or surety products;\n**(C)**\nproviding debt or equity capital or receiving dividends, interest, or distributions of that capital;\n**(D)**\nproviding accounting services;\n**(E)**\nthe sale, lease, or rental of real estate;\n**(F)**\nproviding equipment, parts, substances, or testing services needed to produce cannabis in compliance with the laws and regulations in the applicable State;\n**(G)**\nproviding advertising or marketing services;\n**(H)**\nproviding management consulting services;\n**(I)**\nproviding legal services or compliance services;\n**(J)**\nproviding information technology, software, or communications services;\n**(K)**\nprovision of packaging, transportation, or other logistics services; and\n**(L)**\nunderwriting, dealing, placement or public distribution of securities issued by a cannabis-related legitimate business, including the listing of any such securities on any exchange or trading venue, or any provision of services related to the foregoing.\n**(2) Cannabis**\nThe term cannabis has the meaning given that term in section 6(m)(1) of the Securities Exchange Act of 1934.\n**(3) Cannabis-related legitimate business**\nThe term cannabis-related legitimate business has the meaning given that term in section 6(m)(1) of the Securities Exchange Act of 1934.\n**(4) Financial product or service**\nThe term financial product or service has the meaning given that term in section 1002 of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5481 ).\n**(5) Person**\nThe term person means an individual, a partnership, a corporation, a limited liability company, a business trust, a joint stock company, a trust, an unincorporated association, a joint venture, or any other entity.\n**(6) Service provider**\nThe term service provider has the meaning given that term in section 6(m)(1) of the Securities Exchange Act of 1934.\n**(7) State**\nThe term State means each of the several States, the District of Columbia, each of the territories of the United States, and each Indian Tribe.\n#### 3. Safe harbor for national securities exchanges\nSection 6 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78f ) is amended by adding at the end the following:\n(m) Safe harbor for cannabis-Related legitimate businesses and service providers (1) Definitions In this subsection: (A) Cannabis The term cannabis has the meaning given the term marihuana in section 102 of the Controlled Substances Act ( 21 U.S.C. 802 ). (B) Cannabis product The term cannabis product means any article that contains cannabis, including an article that is a concentrate, an edible, a tincture, a cannabis-infused product, or a topical. (C) Cannabis-related legitimate business The term cannabis-related legitimate business means an issuer that\u2014 (i) initiates, engages, or participates in any business or organized activity that involves cannabis or cannabis products, including cultivating, warehousing, producing, manufacturing, processing, selling, transporting, displaying, dispensing, distributing, or purchasing cannabis or cannabis products; and (ii) engages in the activity described in clause (i) pursuant to a law established by a State or a political subdivision of a State, as determined by that State or political subdivision. (D) Market participant The term market participant means any broker, dealer, underwriter, clearing agency or clearinghouse, securities depository, credit rating agency, alternative trading system, investment adviser, self-regulatory organization, or transfer agent. (E) Service provider The term service provider means\u2014 (i) an issuer that\u2014 (I) sells or otherwise provides goods or services to a cannabis-related legitimate business; or (II) provides any business service relating to cannabis or a cannabis product, including\u2014 (aa) legal, compliance, or accounting services; (bb) sale, leasing, or renting of real estate or equipment; (cc) provision of parts, substances, or testing services needed to produce cannabis in compliance with the laws and regulations in the applicable State; (dd) advertising or marketing services; (ee) management consulting services; (ff) information technology, software, or communications services; and (gg) packaging, transportation, or other logistics services; and (ii) is not a cannabis-related legitimate business. (F) State The term State means each of the several States, the District of Columbia, each of the territories of the United States, and each Indian Tribe. (2) Safe harbor Notwithstanding section 32 of this Act, the Controlled Substances Act ( 21 U.S.C. 801 et seq. ), or any other Federal law, it shall not be unlawful for a national securities exchange registered pursuant to subsection (a) or any market participant to take the following actions in connection with the securities of a cannabis-related legitimate business or a service provider: (A) To have listed, list, or intend to list such securities. (B) To permit the trading of such securities on a national securities exchange. (C) To facilitate the offering, listing, or trading of such securities on a national securities exchange. .\n#### 4. Effective date\nThis Act and the amendment made by this Act shall take effect 180 days after the date of enactment of this Act.",
      "versionDate": "2026-03-18",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-04-02T17:28:38Z"
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
      "date": "2026-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7987ih.xml"
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
      "title": "CLIMB Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-31T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CLIMB Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-31T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Capital Lending and Investment for Marijuana Businesses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-31T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal agencies from taking any adverse action against a person solely because the person provides business assistance to a cannabis-related legitimate business, to amend the Securities Exchange Act of 1934 to create a safe harbor for national securities exchanges to list the securities of issuers that are cannabis-related legitimate businesses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-31T04:48:23Z"
    }
  ]
}
```
