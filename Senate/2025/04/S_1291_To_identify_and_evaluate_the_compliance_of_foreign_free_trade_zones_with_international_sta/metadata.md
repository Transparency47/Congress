# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1291?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1291
- Title: CLEAN FTZ Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1291
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2025-07-01T11:06:18Z
- Update date including text: 2025-07-01T11:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1291",
    "number": "1291",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "CLEAN FTZ Act of 2025",
    "type": "S",
    "updateDate": "2025-07-01T11:06:18Z",
    "updateDateIncludingText": "2025-07-01T11:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T22:12:03Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1291is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1291\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Mr. Cassidy (for himself and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo identify and evaluate the compliance of foreign free trade zones with international standards, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Containing and Limiting the Extensive Abuses Noticed in Free Trade Zones Act of 2025 or the CLEAN FTZ Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Commissioner**\nThe term Commissioner means the Commissioner of U.S. Customs and Border Protection.\n**(2) Illicit international trade**\nThe term illicit international trade means any practice or conduct that\u2014\n**(A)**\nis prohibited by United States law or in violation of relevant international standards, including the guidelines and standards described in section 4(b)(3); and\n**(B)**\nrelates to production, shipment, receipt, possession, distribution, sale, or purchase of any goods, including any practice or conduct intended to facilitate such activity.\n**(3) Non-United States free trade zone; zone**\n**(A) In general**\nThe terms non-United States free trade zone and zone mean a designated area within the customs territory of a foreign country that is treated for purposes of payment of duties or taxes as though the area were located outside the customs territory of that country.\n**(B) Synonymous terms**\nSynonymous terms commonly used to refer to zones described in subparagraph (A) include free zones , special economic zones , export processing zones , free economic zones , and freeports .\n**(4) Person**\nThe term person means an individual or entity.\n#### 3. Identification of international free trade zones\n##### (a) In general\nNot later than 2 years after the date of the enactment of this Act, the Commissioner, in consultation with the Secretary of Commerce, the Secretary of State, the Secretary of the Treasury, and the United States Trade Representative, shall identify and publish, on a publicly accessible internet website, a list of non-United States free trade zones that includes the identity, location, and administrators of each such zone.\n##### (b) Periodic reviews\nThe Commissioner shall review the list of non-United State free trade zones required by subsection (a) on a periodic basis, and not less frequently than annually\u2014\n**(1)**\nto ensure the information included for each zone is correct;\n**(2)**\nto add new zones to the list; and\n**(3)**\nto remove zones no longer in existence from the list.\n#### 4. Classification of countries into tiers\n##### (a) In general\nNot later than 180 days after the list of zones required by section 3 is published, the Commissioner, in consultation with the Secretary of Commerce, the Secretary of State, the Secretary of the Treasury, and the United States Trade Representative, shall publish, on a publicly accessible internet website, a classification of the countries in which those zones are located into tiers as provided by this section.\n##### (b) Methodology\nThe Commissioner shall base the tier classification of countries under subsection (a) on the following standards:\n**(1)**\nMaintenance of a low level of transnational criminal activity in illegally trading narcotics, arms, persons, tobacco, counterfeit consumer goods, commodities, and wildlife occurring in zones located in a country.\n**(2)**\nEffective efforts by the government of the country to counter illicit international trade in zones located in the country, including the effectiveness of penalties and sanctions imposed on countering such trade, compliance with United States and United Nations sanctions regimes, screening practices to detect illicit goods, and eliminating criminal activities related to illicit international trade.\n**(3)**\nThe compliance of zones located in the country with the international guidelines and standards set forth in\u2014\n**(A)**\nthe document of the Organisation for Economic Co-operation and Development entitled Recommendation on Countering Illicit Trade: Enhancing Transparency in Free Trade Zones ;\n**(B)**\nchapter 2 of Specific Annex D of the International Convention on the Simplification and Harmonization of Customs Procedures, done at Kyoto, Japan, on May 18, 1973, as amended by the Protocol of Amendment, done at Brussels, Belgium, on June 26, 1999 (commonly referred to as the Revised Kyoto Convention );\n**(C)**\nthe United Nations Convention against Transnational Organized Crime, done at New York November 15, 2000, and entered into force September 29, 2003 (TIAS 13127);\n**(D)**\nthe United Nations Convention against Illicit Traffic in Narcotic Drugs and Psychotropic Substances, done at Vienna December 20, 1988;\n**(E)**\nthe international standards on combating money laundering and the financing of terrorism and proliferation of the Financial Action Task Force;\n**(F)**\nthe United Nations Convention against Corruption, signed at Merida December 9, 2003;\n**(G)**\nthe Practical Guidance on Free Zones of the World Customs Organization;\n**(H)**\nthe Agreement on Trade Facilitation of the World Trade Organization;\n**(I)**\nthe Agreement on Trade-Related Aspects of Intellectual Property Rights of the World Trade Organization (commonly referred to as the TRIPS Agreement ); and\n**(J)**\nbest practices and guidelines of multilateral export control regimes of which the United States is a member, including practices and guidelines related to implementation of controls on transit and transshipment of export-controlled commodities, software, and technology.\n**(4)**\nSuch other standards as the Commissioner considers relevant.\n##### (c) Tiers\nThe Commissioner, in consultation with the Secretary of Commerce, the Secretary of State, the Secretary of the Treasury, and the United States Trade Representative, shall classify each country in which zones on the list required by section 3 are located into one of the following 4 tiers:\n**(1)**\nCountries with zones that fully comply with standards described in subsection (b) (to be known as tier I countries ).\n**(2)**\nCountries with zones that do not fully comply with those standards but are making significant efforts to bring themselves into compliance with those standards (to be known as tier II countries ).\n**(3)**\nCountries (to be known as tier III countries ) with zones that do not fully comply with those standards and are making efforts to bring themselves into compliance with those standards, but\u2014\n**(A)**\nthe volume of goods or type of goods processed in those zones is significant and the country is not taking proportional concrete actions; or\n**(B)**\nthere is a failure to provide evidence of increasing efforts to combat illicit international trade in those zones from the previous year.\n**(4)**\nCountries with zones that do not comply with those standards and are not making efforts to bring themselves into compliance with those standards (to be known as tier IV countries ).\n##### (d) Publication of classification criteria\nThe Commissioner shall publish the assessment criteria and methodology used to classify countries into the tiers described in subsection (c).\n##### (e) Classification change\n**(1) Progress in meeting standards**\nA tier II, tier III, or tier IV country may be reclassified as a tier I, tier II, or tier III country, respectively, if the zones located in the country show significant progress in complying with the standards described in subsection (b), as determined by the Commissioner, in consultation with the Secretary of Commerce, the Secretary of State, the Secretary of the Treasury, and the United States Trade Representative.\n**(2) Decreasing compliance with standards**\nA tier I, tier II, or tier III country may be reclassified as a tier II, tier III, or tier IV country, respectively, if the zones located in the country show decreasing compliance with the standards described in subsection (b), as determined by the Commissioner, in consultation with the Secretary of Commerce, the Secretary of State, the Secretary of the Treasury, and the United States Trade Representative.\n##### (f) Notification to zones\nNot later than 240 days after publishing the classification of countries required by subsection (a), the Commissioner shall notify the government of each country of the tier to which the country was classified.\n##### (g) Periodic reviews\nThe Commissioner shall review each country in which zones on the list required by section 3 are located on a periodic basis, and not less frequently than annually, to determine whether the country is correctly classified under this section.\n#### 5. Assistance with respect to tier II, tier III, and tier IV countries\n##### (a) In general\nThe Commissioner may provide recommendations and best practice methodologies to countries classified as tier II, tier III, or tier IV countries under section 4 to improve the effectiveness of law enforcement and to combat illicit international trade in the zones located in those countries.\n##### (b) Foreign commercial service strategy\nThe Commissioner shall consider the list of zones required by section 3 in the development of strategies regarding the distribution, priorities, and activities of foreign commercial service officers in countries classified as tier II, tier III, or tier IV countries under section 4.\n##### (c) Scrutiny under sanctions laws\nThe Commissioner shall monitor countries classified as tier II, tier III, or tier IV countries under section 4 to determine if the President may impose the measures under section 6 to ensure greater implementation in the zones located in those countries of the standards described in section 4(b).\n##### (d) Phone hotline and secure website for reporting\nThe Commissioner shall establish and maintain a dedicated, publicly accessible telephone hotline and secure internet website for entities operating in a zone located in a tier I, tier II, tier III, or tier IV country to report instances of illicit international trade in that zone that\u2014\n**(1)**\nimpact or potentially impact their operations; or\n**(2)**\nmay justify reclassification of the country under section 4(e).\n#### 6. Imposition of economic sanctions and visa restrictions with respect to facilitation and support of illicit international trade in tier II, tier III, and tier IV countries\n##### (a) In general\nThe President may impose the measures described in subsection (b) with respect to any foreign person that the President determines, on or after the date of the enactment of this Act and based on credible evidence\u2014\n**(1)**\nhas organized, arranged, financed, conducted, or participated in illicit international trade within a zone located in a country classified as a tier II, tier III, or tier IV country under section 4;\n**(2)**\nhas acted as an agent of or on behalf of another foreign person in facilitating an action leading to illicit international trade occurring in such a zone;\n**(3)**\nhas materially assisted, sponsored, or provided financial, material, or technological support for, or goods or services in support of, illicit international trade occurring in such a zone; or\n**(4)**\nhas conducted or facilitated corruption or money laundering occurring in such a zone.\n##### (b) Measures described\nThe measures described in this subsection are the following:\n**(1) Blocking of property**\nThe President may exercise all of the powers granted to the President under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in property and interests in property of a foreign person described in subsection (a) if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Ineligibility for visas, admission, or parole**\n**(A) Visas, admission, or parole**\nA noncitizen described in subsection (a) is\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\nA noncitizen described in subparagraph (A) is subject to revocation and cancellation, in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ), of any visa or other entry documentation in the possession of the noncitizen, regardless of when the visa or other entry documentation is or was issued.\n##### (c) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section, including investigating, regulating, or prohibiting\u2014\n**(A)**\nany transactions in foreign exchange by any person, or with respect to any property, subject to the jurisdiction of the United States;\n**(B)**\ntransfers of credit or payments between, by, through, or to any banking institution, to the extent that such transfers or payments involve\u2014\n**(i)**\nany interest of any foreign country or national of a foreign country; and\n**(ii)**\nany person, or with respect to any property, subject to the jurisdiction of the United States; and\n**(C)**\nthe importing or exporting of currencies or securities any person, or with respect to any property, subject to the jurisdiction of the United States.\n**(2) Penalties**\nAny person that violates, attempts to violate, conspires to violate, or causes a violation of subsection (b)(1) or a regulation, license, or order issued to carry out that subsection shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n##### (d) Exception To comply with United Nations headquarters agreement and law enforcement objectives\nSubsection (b)(2) shall not apply with respect to a noncitizen if admitting or paroling the noncitizen into the United States\u2014\n**(1)**\nwould further important law enforcement objectives; or\n**(2)**\nis necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations of the United States.\n##### (e) Definitions\nIn this section:\n**(1) Admission; admitted**\nThe terms admission and admitted have the meanings given those terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Foreign person**\nThe term foreign person means an individual or entity that is not a United States person.\n**(3) Noncitizen**\nThe term noncitizen means an individual who is not a citizen or national of the United States (as defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )).\n**(4) United States person**\nThe term United States person means\u2014\n**(A)**\nan individual who is a United States citizen or an alien lawfully admitted for permanent residence to the United States; or\n**(B)**\nan entity organized under the laws of the United States or any jurisdiction within the United States, including a foreign branch of such an entity.\n#### 7. Authorization of appropriations\n##### (a) In general\nThere are authorized to be appropriated to the Commissioner, without fiscal year limitation, such sums as may be necessary to carry out this Act.\n##### (b) Availability of amounts\nAmounts appropriated pursuant to the authorization of appropriations under subsection (a) shall remain available until expended.\n##### (c) Supplement not supplant\nAmounts appropriated pursuant to the authorization of appropriations under subsection (a) shall supplement and not supplant other amounts available for such purposes.",
      "versionDate": "2025-04-03",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-14T16:35:31Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1291is.xml"
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
      "title": "CLEAN FTZ Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-18T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CLEAN FTZ Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-18T03:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Containing and Limiting the Extensive Abuses Noticed in Free Trade Zones Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-18T03:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to identify and evaluate the compliance of foreign free trade zones with international standards, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-18T03:18:26Z"
    }
  ]
}
```
