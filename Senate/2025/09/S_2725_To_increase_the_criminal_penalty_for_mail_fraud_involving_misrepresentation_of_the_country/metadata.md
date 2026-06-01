# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2725?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2725
- Title: STOP Act 2.0
- Congress: 119
- Bill type: S
- Bill number: 2725
- Origin chamber: Senate
- Introduced date: 2025-09-04
- Update date: 2026-03-05T18:08:58Z
- Update date including text: 2026-03-05T18:08:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-04: Introduced in Senate
- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-04: Introduced in Senate

## Actions

- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2725",
    "number": "2725",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "STOP Act 2.0",
    "type": "S",
    "updateDate": "2026-03-05T18:08:58Z",
    "updateDateIncludingText": "2026-03-05T18:08:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-04",
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
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T18:14:37Z",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2725is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2725\nIN THE SENATE OF THE UNITED STATES\nSeptember 4, 2025 Ms. Klobuchar (for herself and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo increase the criminal penalty for mail fraud involving misrepresentation of the country of origin, to terminate the authority to exclude countries from the requirement to transmit advance electronic information for 100 percent of mail shipments under the STOP Act of 2018, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the STOP Act 2.0 .\n#### 2. Criminal penalty for mail fraud involving misrepresentation of country of origin\nSection 1341 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking Whoever and inserting the following:\n(a) In general Whoever ; and\n**(2)**\nby adding at the end the following:\n(b) Misrepresentation of country of origin of international mail shipments (1) In general A person that, in violating subsection (a) or conspiring under section 371 or 1349 to violate subsection (a), knowingly misrepresents the country of origin of an international mail shipment in information required to be submitted under section 343(a) of the Trade Act of 2002 ( 19 U.S.C. 1415(a) ), shall in addition to any other penalty for the offense, be fined under this title, imprisoned not more than 5 years, or both. (2) Seizure and forfeiture The authority of the Department of Homeland Security under subsection (c)(14) of section 592 of the Tariff Act of 1930 ( 19 U.S.C. 1592 ) with respect to seizure and forfeiture shall apply with respect to international mail shipments described in paragraph (1) to the same extent that such authority applies with respect to merchandise entered or attempted to be entered in violation of subsection (a) of such section 592. .\n#### 3. Termination of authority to exclude countries from requirement to transmit advance electronic information for 100 percent of mail shipments\nSection 343(a)(3)(K)(vi) of the Trade Act of 2002 ( 19 U.S.C. 1415(a)(3)(K)(vi) ) is amended by adding at the end the following:\n(V) The authority provided by subclause (II) to exclude a country from the requirement described in subclause (I) shall terminate on the date that is 5 years after the date of the enactment of the STOP Act 2.0 . .\n#### 4. Annual report on compliance with advance electronic information requirements\nSection 8003 of the STOP Act of 2018 (subtitle A of title VIII of Public Law 115\u2013271 ; 132 Stat. 4077) is amended by striking subsections (c) through (f) and inserting the following:\n(c) Annual report on compliance (1) In general Not later than one year after the date of the enactment of the STOP Act 2.0 , and annually thereafter, the Secretary of Homeland Security shall submit to the appropriate congressional committees a report on compliance with the requirements of section 343(a) of the Trade Act of 2002 ( 19 U.S.C. 1415(a) ) that includes the following: (A) An update regarding new and existing agreements reached with foreign postal operators for the transmission of the information required by paragraph (3)(K) of that section. (B) A summary of deliberations between the United States Postal Service and foreign postal operators with respect to issues relating to the transmission of that information. (C) A summary of the progress made in achieving the transmission of that information for the percentage of shipments required by that paragraph, including the results of random checks and information disaggregated by postal and nonpostal data. (D) An assessment of the quality of that information being received by foreign postal operators, as determined by the Secretary, and actions taken to improve the quality of that information, including estimates of\u2014 (i) the amount of information required by section 343(a) of the Trade Act of 2002 that is missing elements, incomplete, inaccurate, or apparently false; (ii) the number of shipments that U.S. Customs and Border Protection requested to be searched as a result of information required by that section; (iii) how many shipments were actually searched pursuant to such a request; and (iv) the results of such searches, including the number of illicit narcotics and counterfeit goods identified during such searches. (E) A description of the results of randomized tests of packages entering the United States to assess the rate of compliance with the requirements of section 343(a) of the Trade Act of 2002\u2014 (i) disaggregated by packages transported by the United States Postal Service and packages transported by private carriers; and (ii) that takes into account, as relevant, the way that the factors set forth in paragraph (3) of that section may affect any differences identified between packages transported by the United States Postal Service and packages transported by private carriers. (F) For each report submitted during the 5-year period beginning on the date of the enactment of the STOP Act 2.0 \u2014 (i) a list of the countries that, during the year preceding submission of the report, were excluded from the requirement under subclause (I) of section 343(a)(3)(K)(vi) of the Trade Act of 2002 that advance information be provided for 100 percent of international mail shipments pursuant to subclause (II) of that section; and (ii) for any country on the list required by clause (i) that has been excluded from the requirement described in that clause for each of the preceding 3 years\u2014 (I) an identification of the reasons why the country remains on the list; and (II) a description of steps that are being taken to ensure that the country is prepared for the termination of the authority to exclude countries from that requirement terminates under subclause (V) of that section (as added by section 3 of the STOP Act 2.0 ). (G) A summary of policies established by the Universal Postal Union that may affect the ability of the Postmaster General to obtain the transmission of the information required by section 343(a) of the Trade Act of 2002. (H) A summary of the use of technology to detect illicit synthetic opioids and other illegal substances in international mail parcels and planned acquisitions and advancements in such technology. (I) Such other information as the Secretary of Homeland Security and the Postmaster General consider appropriate with respect to obtaining the transmission of information required by section 343(a)(3)(K) of the Trade Act of 2002. (2) Form of report (A) In general Each report required by paragraph (1) shall be submitted in unclassified form but may include a classified annex. (B) Public availability The unclassified portion of the report required by paragraph (1) may be made available on a publicly accessible internet website of the United States Postal Service. (3) Appropriate congressional committees defined In this subsection, the term appropriate congressional committees means\u2014 (A) the Committee on the Judiciary and the Committee on Homeland Security and Governmental Affairs of the Senate; and (B) the Committee on the Judiciary and the Committee on Homeland Security of the House of Representatives. .\n#### 5. Public-Private partnerships\nThe Secretary of Homeland Security, the Attorney General, and the Postmaster General may enter into a public-private partnership with private parcel services or other private information technology entities to develop technology and processes for identifying information that could be used to identify the origin of fentanyl, other synthetic opioids, and other narcotics and psychoactive substances, and precursors to such substances, including information on the origin of parcels and shipping information.\n#### 6. International collaboration and information sharing\nThe Secretary of Homeland Security, in consultation with Secretary of State, may, as appropriate, share with and receive from the governments of foreign countries that are allies of the United States, consistent with existing law (including contractual obligations), information with respect to\u2014\n**(1)**\nshippers with a history of transporting illicit fentanyl, other synthetic opioids, and other narcotics and psychoactive substances, and precursors to such substances; and\n**(2)**\nbest practices regarding the detection of such substances, including such substances moving through the mail.\n#### 7. Training of U.S. Customs and Border Protection officers with respect to detecting synthetic opioids\nThe Commissioner of U.S. Customs and Border Protection shall provide to officers of U.S. Customs and Border Protection training in detecting illicit fentanyl, other synthetic opioids, and other narcotics and psychoactive substances, and precursors to such substances, entering the United States, including training with respect to the use of detection equipment and trends in the transportation of such substances.\n#### 8. Evaluation of implementation of STOP Act of 2018\nNot later than one year after the date of the enactment of this Act, the Comptroller General of the United States shall submit to Congress a report evaluating the implementation of the provisions of and amendments made by the STOP Act of 2018 (subtitle A of title VIII of Public Law 115\u2013271 ; 132 Stat. 4073) that includes\u2014\n**(1)**\nidentification of potential areas of risk with respect to the entry of illicit fentanyl, other synthetic opioids, and other narcotics and psychoactive substances into the United States by mail, including any gaps that drug traffickers have found in the system established under the STOP Act of 2018, that takes into account, as relevant, the factors set forth in section 343(a)(3) of the Trade Act of 2002 ( 19 U.S.C. 1415(a)(3) );\n**(2)**\n**(A)**\na description\u2014\n**(i)**\nof any significant differences in rates of compliance with that section between packages transported by the United States Postal Service and packages transported by private carriers; and\n**(ii)**\nthat takes into account, as relevant, the way that the factors set forth in paragraph (3) of that section may affect any such differences; and\n**(B)**\nan analysis of how, if at all, those differences may contribute to the risks identified in paragraph (1); and\n**(3)**\nan assessment of\u2014\n**(A)**\nthe use of the authority provided under subclause (II) of section 343(a)(3)(K)(vi) of the Trade Act of 2002 ( 19 U.S.C. 1415(a)(3)(K)(vi) ) to exclude countries from the requirement under subclause (I) of that section that advance information be provided for 100 percent of international mail shipments; and\n**(B)**\nwhether the use of that authority should be decreased during the period before that authority terminates under subclause (V) of that section (as added by section 3).\n#### 9. Severability\nIf any provision of or amendment made by this Act, or the application of such provision or amendment to any person or circumstance, is held to be unconstitutional, the remainder of the provisions of and amendments made by this Act, and the application of such provisions and amendments to any person or circumstance, shall not be affected.",
      "versionDate": "2025-09-04",
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
        "updateDate": "2025-09-15T17:28:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-04",
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
          "measure-id": "id119s2725",
          "measure-number": "2725",
          "measure-type": "s",
          "orig-publish-date": "2025-09-04",
          "originChamber": "SENATE",
          "update-date": "2026-03-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2725v00",
            "update-date": "2026-03-05"
          },
          "action-date": "2025-09-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>STOP Act 2.0</strong></p><p>This bill revises requirements related to advance electronic data (AED) on international mail shipments. (The STOP Act of 2018 requires international mail shipments coming into the United States to have AED to address the threat of synthetic opioids and other dangerous items.)</p><p>Specifically, the bill establishes a new criminal penalty for knowingly misrepresenting the country of origin of an international mail shipment in order to avoid AED requirements.</p><p>Additionally, five years after enactment, the bill terminates U.S. Customs and Border Protection's (CBP's)\u00a0authority to exclude countries from AED requirements.</p><p>The bill establishes additional reporting requirements related to AED, including a requirement for the Department of Homeland Security (DHS) to report the results of randomized tests of packages entering the United States.</p><p>Further, the bill authorizes DHS, the Department of Justice, and the U.S. Postal Service to enter into partnerships with private parcel services or other private information technology entities to develop technology and processes for identifying the origin of fentanyl, other synthetic opioids, and other narcotics and psychoactive substances.</p><p>The bill also authorizes DHS to share with and receive information from foreign governments regarding (1) shippers with a history of transporting illegal substances, and (2) best practices for detecting the substances.</p><p>CBP must train its officers in detecting illicit fentanyl and other synthetic opioids.</p><p>Finally, the bill directs the Government Accountability Office to evaluate the implementation of the STOP Act of 2018.</p>"
        },
        "title": "STOP Act 2.0"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2725.xml",
    "summary": {
      "actionDate": "2025-09-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>STOP Act 2.0</strong></p><p>This bill revises requirements related to advance electronic data (AED) on international mail shipments. (The STOP Act of 2018 requires international mail shipments coming into the United States to have AED to address the threat of synthetic opioids and other dangerous items.)</p><p>Specifically, the bill establishes a new criminal penalty for knowingly misrepresenting the country of origin of an international mail shipment in order to avoid AED requirements.</p><p>Additionally, five years after enactment, the bill terminates U.S. Customs and Border Protection's (CBP's)\u00a0authority to exclude countries from AED requirements.</p><p>The bill establishes additional reporting requirements related to AED, including a requirement for the Department of Homeland Security (DHS) to report the results of randomized tests of packages entering the United States.</p><p>Further, the bill authorizes DHS, the Department of Justice, and the U.S. Postal Service to enter into partnerships with private parcel services or other private information technology entities to develop technology and processes for identifying the origin of fentanyl, other synthetic opioids, and other narcotics and psychoactive substances.</p><p>The bill also authorizes DHS to share with and receive information from foreign governments regarding (1) shippers with a history of transporting illegal substances, and (2) best practices for detecting the substances.</p><p>CBP must train its officers in detecting illicit fentanyl and other synthetic opioids.</p><p>Finally, the bill directs the Government Accountability Office to evaluate the implementation of the STOP Act of 2018.</p>",
      "updateDate": "2026-03-05",
      "versionCode": "id119s2725"
    },
    "title": "STOP Act 2.0"
  },
  "summaries": [
    {
      "actionDate": "2025-09-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>STOP Act 2.0</strong></p><p>This bill revises requirements related to advance electronic data (AED) on international mail shipments. (The STOP Act of 2018 requires international mail shipments coming into the United States to have AED to address the threat of synthetic opioids and other dangerous items.)</p><p>Specifically, the bill establishes a new criminal penalty for knowingly misrepresenting the country of origin of an international mail shipment in order to avoid AED requirements.</p><p>Additionally, five years after enactment, the bill terminates U.S. Customs and Border Protection's (CBP's)\u00a0authority to exclude countries from AED requirements.</p><p>The bill establishes additional reporting requirements related to AED, including a requirement for the Department of Homeland Security (DHS) to report the results of randomized tests of packages entering the United States.</p><p>Further, the bill authorizes DHS, the Department of Justice, and the U.S. Postal Service to enter into partnerships with private parcel services or other private information technology entities to develop technology and processes for identifying the origin of fentanyl, other synthetic opioids, and other narcotics and psychoactive substances.</p><p>The bill also authorizes DHS to share with and receive information from foreign governments regarding (1) shippers with a history of transporting illegal substances, and (2) best practices for detecting the substances.</p><p>CBP must train its officers in detecting illicit fentanyl and other synthetic opioids.</p><p>Finally, the bill directs the Government Accountability Office to evaluate the implementation of the STOP Act of 2018.</p>",
      "updateDate": "2026-03-05",
      "versionCode": "id119s2725"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2725is.xml"
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
      "title": "STOP Act 2.0",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-10T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "STOP Act 2.0",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-10T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to increase the criminal penalty for mail fraud involving misrepresentation of the country of origin, to terminate the authority to exclude countries from the requirement to transmit advance electronic information for 100 percent of mail shipments under the STOP Act of 2018, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-10T04:18:21Z"
    }
  ]
}
```
