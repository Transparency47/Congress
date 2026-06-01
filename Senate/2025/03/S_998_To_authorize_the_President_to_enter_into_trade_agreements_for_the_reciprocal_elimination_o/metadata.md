# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/998?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/998
- Title: Medical Supply Chain Resiliency Act
- Congress: 119
- Bill type: S
- Bill number: 998
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2025-12-05T22:48:13Z
- Update date including text: 2025-12-05T22:48:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/998",
    "number": "998",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Medical Supply Chain Resiliency Act",
    "type": "S",
    "updateDate": "2025-12-05T22:48:13Z",
    "updateDateIncludingText": "2025-12-05T22:48:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
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
      "actionDate": "2025-03-12",
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
          "date": "2025-03-12T19:56:42Z",
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
      "sponsorshipDate": "2025-03-12",
      "state": "DE"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "TX"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s998is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 998\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Tillis (for himself, Mr. Coons , Mr. Cornyn , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo authorize the President to enter into trade agreements for the reciprocal elimination of duties or other import restrictions with respect to medical goods to contribute to the national security and public health of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Medical Supply Chain Resiliency Act .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nThe COVID\u201319 pandemic created significant demand pressures on the global medical supply chain.\n**(2)**\nAccording to a December 2020 report by the United States International Trade Commission, global demand significantly exceeded available supply of many goods critical for the response to the COVID\u201319 pandemic (in this section referred to as COVID\u201319 critical goods ). Health care providers in the United States faced difficulties in procuring such goods in sufficient quantities. Foreign export restrictions on finished drugs and active pharmaceutical ingredients may have contributed to stress on the supply of some critical COVID\u201319 treatment drugs (including anti-infective products), as well as hormone medications and vitamins.\n**(3)**\nAccording to the McKinsey Global Institute, during the 20 years preceding the date of the enactment of this Act, pharmaceutical supply chains have become more globally dispersed and many generic small-molecule products have shifted to lower-cost production locations, some of which have been identified as posing a threat to the national security of the United States.\n**(4)**\nAccording to the Organisation for Economic Co-operation and Development, while the United States is one of the largest exporters of COVID\u201319 critical goods, it is also one of the largest importers of those goods.\n**(5)**\nThe World Trade Organization has found that, while the United States, Germany, and the People's Republic of China are all major producers and importers of COVID\u201319 critical goods, United States import partners are less diversified compared to Germany and the People's Republic of China. In the United States, more than half of its imports of COVID\u201319 critical goods came from only 3 partners\u2014the People's Republic of China (30.6 percent), Mexico (15.3 percent), and Malaysia (9.0 percent).\n**(6)**\nWhile some of the countries in which medical supply manufacturing occurs are reliable suppliers and allies to the United States, others have adopted or maintained policies that make United States supply less secure.\n##### (b) Sense of Congress\nIt is the sense of Congress that, given the threat to national security and public health that could arise if the United States is unable to swiftly respond to significant demand surges for medical products in a future pandemic, it is critical that the United States diversify its trade relationships and prioritize partners that adopt and maintain reliable supply chain policies.\n#### 3. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto improve overall medical supply chain resilience for the United States by establishing a framework to enhance medical supply chains with trusted trade partners;\n**(2)**\nto enhance supply chain security related to technology transfer and intellectual property protection;\n**(3)**\nto diversify and expand supplier networks to ensure a reliable supply of medical goods, especially in the event of emergency situations;\n**(4)**\nto eliminate unnecessary trade barriers and distortions that weaken or disrupt medical supply chains;\n**(5)**\nto expedite cross-border movement of critical medical goods;\n**(6)**\nto foster international collaboration, encourage new investments, promote cooperation and partnership in public and private research and development efforts, facilitate data flows for life science research and development, and expand manufacturing capacities for medical devices and pharmaceutical goods;\n**(7)**\nto promote regulatory cooperation with respect to manufacturing of medical goods;\n**(8)**\nto increase access to government procurement markets for medical goods;\n**(9)**\nto encourage adoption of and adherence to good regulatory practices related to medical goods;\n**(10)**\nto enable greater transparency, regulatory harmonization, and reliance in authorization and licensing procedures for medical devices and pharmaceutical goods;\n**(11)**\nto facilitate trade in medical goods to the most efficient and practicable extent possible; and\n**(12)**\nto identify current production capacities, address potential weaknesses, and improve overall resilience.\n#### 4. Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Finance of the Senate; and\n**(B)**\nthe Committee on Ways and Means of the House of Representatives.\n**(2) Country**\nThe term country means\u2014\n**(A)**\nany foreign country or territory, including any overseas dependent territory or possession of a foreign country; or\n**(B)**\nthe Trust Territory of the Pacific Islands.\n**(3) Medical device**\nThe term medical device means a device, as defined in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ), that is intended for use in humans.\n**(4) Medical good**\nThe term medical good means any medical device, pharmaceutical good, or input for such a device or good.\n**(5) Medical supply chain**\nThe term medical supply chain means any activities involving design, procurement, manufacturing, production, distribution, operation, or management related to medical goods.\n**(6) Pharmaceutical good**\nThe term pharmaceutical good means a drug, as defined in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ), that is intended for use in humans.\n**(7) Trade Representative**\nThe term Trade Representative means the United States Trade Representative.\n**(8) Trusted trade partner**\nThe term trusted trade partner means any country that has entered into an agreement with the United States under section 5.\n**(9) Trusted trade partner agreement**\nThe term trusted trade partner agreement means an agreement entered into under section 5.\n#### 5. Authority to enter into trusted trade partner agreements\n##### (a) In general\nWhenever the President determines, based on the considerations set forth in subsection (b), that the reciprocal elimination of existing duties or other import restrictions of a country or countries and the United States with respect to medical goods would contribute to the national security and public health of the United States, the President may, subject to the requirements under section 6\u2014\n**(1)**\nnegotiate, enter into, and enforce a trusted trade partner agreement with the country or countries; and\n**(2)**\nproclaim such modification of any existing duty, such continuance of existing duty-free or excise treatment, or such additional duties, as the President determines to be required or appropriate to carry out any such trade agreement.\n##### (b) Considerations\nIn determining whether to enter into negotiations for a trusted trade partner agreement with a country pursuant to subsection (a), the President shall take into account whether the government of the country has\u2014\n**(1)**\nexpressed a desire to enter into such an agreement;\n**(2)**\ndemonstrated a commitment to contribute to global health security, including the national security of the United States and the health of United States citizens, by maintaining open trade in medical goods during a public health emergency, including to enable research, development, and manufacturing of those goods;\n**(3)**\nadhered to and implemented the commitments and obligations under existing free trade agreements to which that country and the United States are parties;\n**(4)**\nimplemented measures to reduce or eliminate unnecessary trade barriers and distorting practices affecting medical goods;\n**(5)**\nmaintained the rule of law by enacting and enforcing laws and regulations in a clear, publicized, transparent, and nondiscriminatory manner;\n**(6)**\nadopted and enforced laws that provide adequate and effective protection of intellectual property rights reflecting a standard of protection similar to that found under United States law; and\n**(7)**\nagreed to recognize and promote good regulatory practices related to medical goods.\n##### (c) Trusted trade partner agreements\nA trusted trade partner agreement may, with respect to medical goods, provide for\u2014\n**(1)**\nreduction or elimination of duties, quotas, and other trade barriers that undermine the national security and public health of the United States by disincentivizing research, development, and manufacturing in the United States or in countries that are reliable suppliers of medical goods to the United States;\n**(2)**\ndiversification and expansion of supplier networks to secure a reliable supply of medical goods;\n**(3)**\nharmonization or convergence of regulatory procedures, regulatory reliance, inspection cooperation, and adoption of international standards (such as to streamline post-approval changes) to expedite cross-border movement of medical goods;\n**(4)**\nincreased access to government procurement markets for medical goods and, in the case of a multilateral agreement entered into under the auspices of the World Trade Organization, membership in the Agreement on Government Procurement of the World Trade Organization referred to in section 101(d)(17) of the Uruguay Round Agreements Act ( 19 U.S.C. 3511(d)(17) );\n**(5)**\nadequate and effective protection of intellectual property rights for medical goods reflecting a standard of protection similar to that found under United States law;\n**(6)**\nregulatory cooperation on manufacturing standards for medical goods;\n**(7)**\na collaboration framework to promote public and private research and development efforts related to medical goods, including facilitation of data flows for life science research and development;\n**(8)**\nadherence to good regulatory practices for sound, affordable, and efficient regulation of medical goods;\n**(9)**\npromotion of regulatory compatibility and cooperation to facilitate trade and investment related to medical goods and accelerate manufacturing of such goods during a public health emergency; and\n**(10)**\nexemption of parties to the agreement from trade-restrictive measures imposed with respect to medical goods during a public health emergency.\n##### (d) Report required\nNot later than 180 days after the date of the enactment of this Act, and every 180 days thereafter, the President shall submit to Congress a report on the status of negotiations conducted under subsection (a) for trusted trade partner agreements.\n#### 6. Congressional oversight, notice, consultations, access to information, and review\n##### (a) Notice\nNot later than 60 days before initiating negotiations with a trusted trade partner under section 5(a) for a trusted trade partner agreement, the President shall submit to Congress written notice of the intention of the President to enter into the negotiations, which shall include the date negotiations will begin and the trusted trade partner with whom the President seeks to enter into the agreement.\n##### (b) Consultation with members of Congress\n**(1) Consultation during negotiations and access to information**\nIn the course of negotiations under section 5(a) for a trusted trade partner agreement, the Trade Representative shall\u2014\n**(A)**\nmeet upon request with the appropriate committees of Congress regarding negotiating objectives, the status of negotiations in progress, and potential effects to the laws of the United States with respect to the agreement;\n**(B)**\nupon request by the appropriate committees of Congress, provide access to pertinent documents relating to the negotiations; and\n**(C)**\nconsult closely and on a timely basis with, and keep fully apprised of the negotiations, the appropriate committees of Congress.\n**(2) Consultation before entry into agreement**\nBefore entering into a trusted trade partner agreement under section 5, the Trade Representative shall consult with\u2014\n**(A)**\nthe appropriate committees of Congress; and\n**(B)**\neach other committee of the Senate and the House of Representatives, and each joint committee of Congress, that has jurisdiction over legislation involving a subject matter that would be affected by the agreement.\n##### (c) Consultation with Federal agencies\nIn the course of negotiations under section 5(a) for a trusted trade partner agreement, the Trade Representative shall inform and consult with any Federal agency having expertise in the matters being negotiated, including the Department of Health and Human Services.\n##### (d) Limitation on action\nAny duty elimination or staged rate reduction provided for under section 5 may be proclaimed only if the President\u2014\n**(1)**\nhas obtained advice regarding the proposed action from the appropriate advisory committees established under section 135 of the Trade Act of 1974 ( 19 U.S.C. 2155 ) and the International Trade Commission;\n**(2)**\nhas submitted to the appropriate committees of Congress a report that sets forth\u2014\n**(A)**\nthe action proposed to be proclaimed;\n**(B)**\nthe reasons for such action; and\n**(C)**\nthe advice obtained under paragraph (1); and\n**(3)**\nhas consulted with the appropriate committees of Congress regarding the proposed action during the 60-day period on the date on which the President has met the requirements under paragraphs (1) and (2).\n##### (e) Report to Congress\nNot later than 60 days before the date on which the President enters into a trusted trade partner agreement with a trusted trade partner under section 5, the President shall submit to Congress a report describing\u2014\n**(1)**\nthe nature and scope of the agreement;\n**(2)**\nthe proposed duration of the agreement;\n**(3)**\nhow and to what extent the agreement will achieve the applicable purposes, policies, priorities, and objectives of this Act;\n**(4)**\nwhether sufficient evidence exists demonstrating that\u2014\n**(A)**\nthe trusted trade partner satisfies the conditions under section 5(b); and\n**(B)**\nthe reciprocal elimination of existing duties or other import restrictions of the trusted trade partner or the United States with respect to medical goods would contribute to the national security and public health of the United States; and\n**(5)**\nthe proposed implementation of the agreement, including the general effect of the agreement on existing laws.\n##### (f) Congressional right To review and disapprove\n**(1) In general**\nA trusted trade partner agreement shall not take effect until\u2014\n**(A)**\nthe proposed agreement has been submitted to Congress, together with the report required under subsection (e) with respect to that agreement; and\n**(B)**\nthe review period required under paragraph (2) following the date on which the proposed agreement has been submitted to Congress under subparagraph (A) has been exhausted, during which period a joint resolution is not enacted under paragraph (4).\n**(2) Review**\n**(A) Initial review**\nUnless extended under subparagraph (B) or (C), the review period under this paragraph with respect to a trusted trade partner agreement is 30 days, during which time Congress shall review the proposed agreement with respect to whether\u2014\n**(i)**\nthe President failed or refused to provide notice with respect to the agreement in accordance with subsection (a);\n**(ii)**\nthe President failed or refused to consult with respect to the agreement in accordance with subsections (b) and (c);\n**(iii)**\nthe President failed or refused to submit to Congress a report with respect to the agreement in accordance with subsection (e); or\n**(iv)**\nthe President failed or refused to demonstrate that the agreement would achieve the applicable purposes, policies, priorities, and objectives of this Act and contribute to the national security and public health of the United States.\n**(B) Further review**\nIf, during the 30-day period under subparagraph (A) with respect to a trusted trade partner agreement, one House of Congress adopts a resolution stating that the House of Congress wishes to further review the proposed agreement, the review period under this paragraph with respect to the proposed agreement shall be extended by a period of 60 days, during which time the appropriate committees of Congress shall engage the President with respect to the proposed agreement and the failures or refusals of the President specified under subparagraph (A).\n**(C) Additional period**\nIf, during the 60-day period under subparagraph (B) with respect to a trusted trade partner agreement, one House of Congress adopts a resolution stating that the House of Congress wishes to further review the proposed agreement, the review period under this paragraph with respect to the proposed agreement shall be further extended by a period of 30 days.\n**(3) Procedures for considering resolutions**\nA resolution under subparagraph (B) or (C) of paragraph (2)\u2014\n**(A)**\nin the Senate\u2014\n**(i)**\nmay be introduced by any Member of the Senate;\n**(ii)**\nshall be referred to the Committee on Finance; and\n**(iii)**\nmay not be amended;\n**(B)**\nin the House of Representatives\u2014\n**(i)**\nmay be introduced by any Member of the House;\n**(ii)**\nshall be referred to the Committee on Ways and Means or the Committee on Rules; and\n**(iii)**\nmay not be amended by either Committee; and\n**(C)**\nthe vote on passage of the resolution shall occur immediately following the conclusion of the debate on the trusted trade partner agreement at issue and a single quorum call at the conclusion of the debate.\n**(4) Disapproval**\nIf, during the review period required under paragraph (2) with respect to a trusted trade partner agreement, a joint resolution is enacted stating that Congress does not favor the agreement, the agreement shall not take effect.\n#### 7. Monitoring and enforcement of continued compliance with trusted trade partner agreements\n##### (a) Monitoring\nThe Trade Representative shall periodically monitor compliance by a trusted trade partner with the commitments and obligations of the partner under a trusted trade partner agreement.\n##### (b) Actions in response to failure To comply\n**(1) Determination and report of Trade Representative**\nIf the Trade Representative determines that a trusted trade partner has failed to satisfactorily implement, maintain, and enforce the commitments and obligations of the partner under a trusted trade partner agreement, the Trade Representative shall submit to the President a report setting forth\u2014\n**(A)**\nthe determination and the findings that support the determination; and\n**(B)**\nbased on such findings, the recommendations of the Trade Representative for action or inaction under this subsection.\n**(2) Determination of President**\nNot later than 30 days after receiving a report under paragraph (1) with respect to a trusted trade partner, the President shall\u2014\n**(A)**\ndetermine whether the President concurs with the determination of the Trade Representative set forth in the report; and\n**(B)**\nif the President concurs, determine whether\u2014\n**(i)**\nto suspend, withdraw, or prevent the application of the trusted trade partner agreement with the trusted trade partner;\n**(ii)**\nto enter into a binding agreement with the partner that commits the partner\u2014\n**(I)**\nto eliminate any burden or restriction on the United States resulting from the failure of the partner to comply with the commitments and obligations of the partner under a trusted trade partner agreement; and\n**(II)**\nto provide the United States with such compensatory trade benefits as are negotiated between the Trade Representative and the partner; or\n**(iii)**\nto take such other actions as the Trade Representative considers necessary to encourage the partner to adhere to the commitments and obligations of the partner under a trusted trade partner agreement, including suspending the exemption of the partner from trade-restrictive measures imposed with respect to medical goods during a public health emergency.\n**(3) Timeline for action**\nIf the President determines under paragraph (2)(B) to take action, the President shall implement that action by not later than the date that is 15 days after the day on which the President determines to take action under that paragraph.",
      "versionDate": "2025-03-12",
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
        "actionDate": "2025-03-18",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2213",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Medical Supply Chain Resiliency Act",
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
        "updateDate": "2025-05-12T18:04:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-12",
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
          "measure-id": "id119s998",
          "measure-number": "998",
          "measure-type": "s",
          "orig-publish-date": "2025-03-12",
          "originChamber": "SENATE",
          "update-date": "2025-06-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s998v00",
            "update-date": "2025-06-24"
          },
          "action-date": "2025-03-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Medical Supply Chain Resiliency Act</strong></p><p>This bill authorizes actions to facilitate trade in medical goods (i.e., medical devices, pharmaceutical goods, or inputs for such devices or goods).</p><p>Specifically, the bill authorizes the President to (1) negotiate, enter into, and enforce a trusted trade partner agreement with a country or countries with respect to medical goods; and (2) proclaim a modification of any existing duty, a continuance of existing duty-free or excise treatment, or additional duties to carry out the trade agreement. These actions may only be taken if the President determines, based on specified considerations, that the reciprocal elimination of existing duties or other import restrictions with respect to medical goods would contribute to\u00a0U.S. national security and public health.\u00a0</p><p>A trusted trade partner agreement may include certain provisions, such as those to (1) reduce or eliminate duties, quotas, or other trade barriers; (2) diversify and expand supplier networks to secure a reliable supply of medical goods; and (3) harmonize regulatory procedures.</p><p>Not later than 60 days before initiating negotiations with a trusted trade partner, the President must submit written notice to Congress. The bill requires congressional consultation and review of these trade agreements. A trade agreement shall not take effect if, during the required review period, Congress enacts a joint resolution of disapproval.</p><p>The Office of the\u00a0U.S. Trade Representative must monitor compliance by a trusted trade partner with the trade agreement's commitments and obligations. Further, the President may take certain actions in response to a failure to comply. \u00a0 \u00a0</p>"
        },
        "title": "Medical Supply Chain Resiliency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s998.xml",
    "summary": {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Medical Supply Chain Resiliency Act</strong></p><p>This bill authorizes actions to facilitate trade in medical goods (i.e., medical devices, pharmaceutical goods, or inputs for such devices or goods).</p><p>Specifically, the bill authorizes the President to (1) negotiate, enter into, and enforce a trusted trade partner agreement with a country or countries with respect to medical goods; and (2) proclaim a modification of any existing duty, a continuance of existing duty-free or excise treatment, or additional duties to carry out the trade agreement. These actions may only be taken if the President determines, based on specified considerations, that the reciprocal elimination of existing duties or other import restrictions with respect to medical goods would contribute to\u00a0U.S. national security and public health.\u00a0</p><p>A trusted trade partner agreement may include certain provisions, such as those to (1) reduce or eliminate duties, quotas, or other trade barriers; (2) diversify and expand supplier networks to secure a reliable supply of medical goods; and (3) harmonize regulatory procedures.</p><p>Not later than 60 days before initiating negotiations with a trusted trade partner, the President must submit written notice to Congress. The bill requires congressional consultation and review of these trade agreements. A trade agreement shall not take effect if, during the required review period, Congress enacts a joint resolution of disapproval.</p><p>The Office of the\u00a0U.S. Trade Representative must monitor compliance by a trusted trade partner with the trade agreement's commitments and obligations. Further, the President may take certain actions in response to a failure to comply. \u00a0 \u00a0</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119s998"
    },
    "title": "Medical Supply Chain Resiliency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Medical Supply Chain Resiliency Act</strong></p><p>This bill authorizes actions to facilitate trade in medical goods (i.e., medical devices, pharmaceutical goods, or inputs for such devices or goods).</p><p>Specifically, the bill authorizes the President to (1) negotiate, enter into, and enforce a trusted trade partner agreement with a country or countries with respect to medical goods; and (2) proclaim a modification of any existing duty, a continuance of existing duty-free or excise treatment, or additional duties to carry out the trade agreement. These actions may only be taken if the President determines, based on specified considerations, that the reciprocal elimination of existing duties or other import restrictions with respect to medical goods would contribute to\u00a0U.S. national security and public health.\u00a0</p><p>A trusted trade partner agreement may include certain provisions, such as those to (1) reduce or eliminate duties, quotas, or other trade barriers; (2) diversify and expand supplier networks to secure a reliable supply of medical goods; and (3) harmonize regulatory procedures.</p><p>Not later than 60 days before initiating negotiations with a trusted trade partner, the President must submit written notice to Congress. The bill requires congressional consultation and review of these trade agreements. A trade agreement shall not take effect if, during the required review period, Congress enacts a joint resolution of disapproval.</p><p>The Office of the\u00a0U.S. Trade Representative must monitor compliance by a trusted trade partner with the trade agreement's commitments and obligations. Further, the President may take certain actions in response to a failure to comply. \u00a0 \u00a0</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119s998"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s998is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the President to enter into trade agreements for the reciprocal elimination of duties or other import restrictions with respect to medical goods to contribute to the national security and public health of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:32Z"
    },
    {
      "title": "Medical Supply Chain Resiliency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Medical Supply Chain Resiliency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:21Z"
    }
  ]
}
```
