# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3399?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3399
- Title: Digital Trade Promotion Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3399
- Origin chamber: Senate
- Introduced date: 2025-12-09
- Update date: 2026-01-07T16:24:26Z
- Update date including text: 2026-01-07T16:24:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in Senate
- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-12-09: Introduced in Senate

## Actions

- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3399",
    "number": "3399",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Digital Trade Promotion Act of 2025",
    "type": "S",
    "updateDate": "2026-01-07T16:24:26Z",
    "updateDateIncludingText": "2026-01-07T16:24:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T19:48:33Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "DE"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "KS"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3399is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3399\nIN THE SENATE OF THE UNITED STATES\nDecember 9, 2025 Mr. Young (for himself, Mr. Coons , Mr. Moran , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo authorize the President to enter into digital trade agreements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Digital Trade Promotion Act of 2025 .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nThe Bureau of Economic Analysis found that the digital economy contributed roughly 10 percent of United States gross domestic product and supported approximately 8,900,000 United States jobs in 2022.\n**(2)**\nIn 2023, United States exports of digital services surpassed $655,000,000,000, accounting for more than half of all United States services exports and generating a digital services trade surplus for the United States of roughly $266,800,000,000.\n**(3)**\nDigital trade bolsters the economy by enabling the sale of goods and the supply of services across borders.\n**(4)**\nDigital trade has become increasingly vital to United States workers and businesses of all sizes, including manufacturers, farmers, industrial facilities, service suppliers, and countless small and medium-sized enterprises that use digital technology to produce and export goods and services across the world.\n**(5)**\nDigital trade is crucial for the global competitiveness of the United States, as United States industry relies on free and secure cross-border data flows to deploy cutting-edge technology essential to innovation and productivity.\n**(6)**\nDigital innovation has provided new opportunities for economic development, entrepreneurship, and growth in developing countries around the world.\n**(7)**\nCountries have negotiated international rules governing digital trade in various bilateral and plurilateral agreements, but those rules remain fragmented.\n**(8)**\nThe United States, through free trade agreements and trade negotiations, has been a leader in developing rules and standards governing digital trade and electronic commerce that have helped the United States and partners of the United States unlock the economic potential of digital innovation.\n**(9)**\nCertain countries, including the People\u2019s Republic of China, are advancing discriminatory digital policies that undermine United States companies and workers by enabling censorship, surveillance, forced technology transfers, and data flow restrictions at the expense of human rights, the rule of law, privacy, and an open internet.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthere is a need for agreements on digital trade, as Congress recognized by its support for a robust digital trade chapter in the United States-Mexico-Canada Agreement, which has been of critical importance to all sectors of the economy;\n**(2)**\nnegotiating strong digital trade principles and commitments with countries across the globe enables the United States to unite like-minded countries around common standards and ensure that principles of democracy, rule of law, freedom of speech, human and worker rights, privacy, and a free and open internet are at the very core of digital governance; and\n**(3)**\neven as domestic statutes and regulations governing the digital economy continue to develop and evolve, the United States should cooperate with its allies and trading partners to advance global digital trade rules that reflect United States interests and values.\n#### 3. Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Finance of the Senate; and\n**(B)**\nthe Committee on Ways and Means of the House of Representatives.\n**(2) Country**\nThe term country means any foreign country or territory, including any overseas dependent territory or possession of a foreign country.\n**(3) Trade Representative**\nThe term Trade Representative means the United States Trade Representative.\n**(4) Digital trade agreement**\nThe term digital trade agreement means an agreement with one or more trusted trade partners entered into under section 4.\n#### 4. Authority to enter into digital trade agreements\n##### (a) In general\nThe President may, subject to the requirements under section 5, negotiate, enter into, and enforce a digital trade agreement with a country or countries.\n##### (b) Considerations\nIn determining whether to enter into negotiations for a digital trade agreement with a country pursuant to subsection (a), the President shall take into account whether the government of the country has\u2014\n**(1)**\nexpressed a desire to enter into such an agreement;\n**(2)**\nadhered to and implemented the commitments and obligations under any existing free trade agreements to which that country and the United States are parties;\n**(3)**\nimplemented measures to reduce or eliminate unnecessary trade barriers and distorting practices affecting electronic commerce;\n**(4)**\nmaintained the rule of law by enacting and enforcing laws and regulations in a clear, publicized, transparent, and nondiscriminatory manner; and\n**(5)**\nadopted and enforced laws that provide adequate and effective protection of intellectual property rights reflecting a standard of protection similar to that found under United States law.\n##### (c) Content of digital trade agreements\nA digital trade agreement shall apply to all sectors of the economy and provide for\u2014\n**(1)**\nnondiscriminatory treatment of digital products and digital services;\n**(2)**\nprohibition of discriminatory taxes on digital services;\n**(3)**\nthe free flow of data across borders and the prohibition of data localization requirements;\n**(4)**\nframeworks for the secure transfer and sharing of industrial data and other sensitive data that bolster data security, including through the promotion and protection of end-to-end encryption;\n**(5)**\nthe protection of consumers engaged in electronic commerce, including the promotion of interoperability mechanisms, such as the Cross-Border Privacy Rules of the Asia-Pacific Economic Cooperation, or successor frameworks, to facilitate international data transfers while ensuring the protection of the privacy of personal information;\n**(6)**\nprohibition of forced transfer or disclosure of source code, algorithms, cryptographic technology, trade secrets, and other proprietary technology as a condition of market access;\n**(7)**\ncooperation to advance interoperable, risk-based frameworks for the development, deployment, and cross-border trade in emerging digital technologies, including artificial intelligence and quantum computing;\n**(8)**\ncooperation in addressing cybersecurity threats and adherence to risk-based approaches to mitigating cybersecurity threats, including sharing of information and coordination on incident response and best practices based on consensus standards;\n**(9)**\nprohibition of customs duties on electronic transmissions, including on content transmitted electronically;\n**(10)**\npromotion of voluntary, international standards for digital technologies and services;\n**(11)**\npromotion of alignment on export controls, sanctions, and investment review mechanisms that impact digital trade;\n**(12)**\ngreater transparency in domestic regulation of services;\n**(13)**\npromotion of risk-based approaches to government procurement of hardware and software to support secure digital infrastructure;\n**(14)**\nother provisions that, in the judgment of the Trade Representative, would advance the national interests of the United States with respect to digital trade; and\n**(15)**\nexceptions to the provisions described in paragraphs (1) through (14) to allow for the protection of legitimate public policy objectives and national security.\n#### 5. Congressional oversight, notice, consultations, access to information, and review\n##### (a) Notice\nNot later than 60 days before initiating negotiations with a country under section 4(a) for a digital trade agreement, the President shall submit to Congress written notice of the intention of the President to enter into the negotiations, which shall include the date on which negotiations will begin and the country with which the President seeks to enter into the agreement.\n##### (b) Consultation with members of Congress\n**(1) Consultation during negotiations and access to information**\nIn the course of negotiations under section 4(a) for a digital trade agreement, the Trade Representative shall\u2014\n**(A)**\nmeet upon request with the appropriate committees of Congress regarding negotiating objectives, the status of negotiations in progress, and potential effects to the laws of the United States resulting from the agreement;\n**(B)**\nupon request by the appropriate committees of Congress, provide access to pertinent documents relating to the negotiations; and\n**(C)**\nconsult closely and on a timely basis with, and keep fully apprised of the negotiations, the appropriate committees of Congress.\n**(2) Consultation before entry into agreement**\nBefore entering into a digital trade agreement under section 4, the Trade Representative shall consult with\u2014\n**(A)**\nthe appropriate committees of Congress; and\n**(B)**\neach other committee of the Senate and the House of Representatives, and each joint committee of Congress, that has jurisdiction over legislation involving a subject matter that would be affected by the agreement.\n##### (c) Consultation with Federal agencies\nIn the course of negotiations under section 4(a) for a digital trade agreement, the Trade Representative shall inform and consult with any Federal agency having expertise in the matters being negotiated.\n##### (d) Report to Congress\nNot later than 60 days before the date on which the President enters into a digital trade agreement with a country under section 4, the President shall submit to Congress a report describing\u2014\n**(1)**\nthe nature and scope of the agreement;\n**(2)**\nthe proposed duration of the agreement;\n**(3)**\nhow and to what extent the agreement will achieve the applicable purposes, policies, priorities, and objectives of this Act;\n**(4)**\nwhether sufficient evidence exists demonstrating that the country satisfies the conditions under section 4(b); and\n**(5)**\nthe proposed implementation of the agreement, including the general effect of the agreement on existing laws.\n##### (e) Congressional right To review and disapprove\n**(1) In general**\nA digital trade agreement shall not take effect until\u2014\n**(A)**\nthe proposed agreement and the report required by subsection (d) with respect to that agreement have been submitted to Congress; and\n**(B)**\nthe review period required by paragraph (2) following the date on which the proposed agreement has been submitted to Congress under subparagraph (A) has been exhausted, during which period a joint resolution is not enacted under paragraph (4).\n**(2) Review**\n**(A) Initial review**\nUnless extended under subparagraph (B) or (C), the review period under this paragraph with respect to a digital trade agreement is 30 days, during which time Congress shall review\u2014\n**(i)**\nthe proposed agreement; and\n**(ii)**\nwhether\u2014\n**(I)**\nthe President failed or refused to provide notice with respect to the agreement in accordance with subsection (a);\n**(II)**\nthe President failed or refused to consult with respect to the agreement in accordance with subsections (b) and (c);\n**(III)**\nthe President failed or refused to submit to Congress a report with respect to the agreement in accordance with subsection (d); or\n**(IV)**\nthe President failed or refused to demonstrate that the agreement would achieve the applicable purposes, policies, priorities, and objectives of this Act.\n**(B) Further review**\nIf, during the 30-day period under subparagraph (A) with respect to a digital trade agreement, one House of Congress adopts a resolution stating that the House of Congress wishes to further review the proposed agreement, the review period under this paragraph with respect to the proposed agreement shall be extended by a period of 60 days, during which time the appropriate committees of Congress shall engage the President with respect to the proposed agreement and the failures or refusals of the President specified under subparagraph (A).\n**(C) Additional period**\nIf, during the 60-day period under subparagraph (B) with respect to a digital trade agreement, one House of Congress adopts a resolution stating that the House of Congress wishes to further review the proposed agreement, the review period under this paragraph with respect to the proposed agreement shall be further extended by a period of 30 days.\n**(3) Procedures for considering resolutions**\nA resolution under subparagraph (B) or (C) of paragraph (2)\u2014\n**(A)**\nin the Senate\u2014\n**(i)**\nmay be introduced by any Member of the Senate;\n**(ii)**\nshall be referred to the Committee on Finance; and\n**(iii)**\nmay not be amended;\n**(B)**\nin the House of Representatives\u2014\n**(i)**\nmay be introduced by any Member of the House;\n**(ii)**\nshall be referred to the Committee on Ways and Means or the Committee on Rules; and\n**(iii)**\nmay not be amended by either Committee; and\n**(C)**\nthe vote on passage of the resolution shall occur immediately following the conclusion of the debate on the digital trade agreement at issue and a single quorum call at the conclusion of the debate.\n**(4) Disapproval**\nIf, during the review period required under paragraph (2) with respect to a digital trade agreement, a joint resolution is enacted stating that Congress does not favor the agreement, the agreement shall not take effect.\n#### 6. Monitoring and enforcement of continued compliance with digital trade agreements\n##### (a) Monitoring\nThe Trade Representative shall periodically monitor compliance by a country with the commitments and obligations of the country under a digital trade agreement.\n##### (b) Actions in response to failure To comply\n**(1) Determination and report of trade representative**\nIf the Trade Representative determines that a country has failed to satisfactorily implement, maintain, and enforce the commitments and obligations of the country under a digital trade agreement, the Trade Representative shall submit to the President a report setting forth\u2014\n**(A)**\nthe determination and the findings that support the determination; and\n**(B)**\nbased on such findings, the recommendations of the Trade Representative for action or inaction under this subsection.\n**(2) Determination of President**\nNot later than 30 days after receiving a report under paragraph (1) with respect to a country, the President shall\u2014\n**(A)**\ndetermine whether the President concurs with the determination of the Trade Representative set forth in the report; and\n**(B)**\nif the President concurs, determine whether\u2014\n**(i)**\nto suspend, withdraw, or prevent the application of the digital trade agreement with the country;\n**(ii)**\nto enter into a binding agreement with the country that commits the country\u2014\n**(I)**\nto eliminate any burden or restriction on the United States resulting from the failure of the country to comply with the commitments and obligations of the country under a digital trade agreement; and\n**(II)**\nto provide the United States with such compensatory trade benefits as are negotiated between the Trade Representative and the country; or\n**(iii)**\nto take such other actions as the Trade Representative considers necessary to encourage the country to adhere to the commitments and obligations of the country under a digital trade agreement.\n**(3) Timeline for action**\nIf the President determines under paragraph (2)(B) to take action, the President shall implement that action by not later than the date that is 15 days after the day on which the President determines to take action under that paragraph.",
      "versionDate": "2025-12-09",
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
        "updateDate": "2026-01-07T16:24:26Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3399is.xml"
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
      "title": "Digital Trade Promotion Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-31T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Digital Trade Promotion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the President to enter into digital trade agreements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:33:15Z"
    }
  ]
}
```
