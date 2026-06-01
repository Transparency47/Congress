# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1492?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1492
- Title: Deploying American Blockchains Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1492
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-04-21T13:46:14Z
- Update date including text: 2026-04-21T13:46:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-04-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-07-09 - Committee: Committee on Banking, Housing, and Urban Affairs. Hearings held.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-84.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-84.
- 2025-10-21 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 195.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-04-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-07-09 - Committee: Committee on Banking, Housing, and Urban Affairs. Hearings held.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-84.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-84.
- 2025-10-21 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 195.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1492",
    "number": "1492",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001242",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Moreno, Bernie [R-OH]",
        "lastName": "Moreno",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Deploying American Blockchains Act of 2025",
    "type": "S",
    "updateDate": "2026-04-21T13:46:14Z",
    "updateDateIncludingText": "2026-04-21T13:46:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-21",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 195.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-84.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-21",
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
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-84.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-09",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Banking, Housing, and Urban Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
            "date": "2025-10-21T18:36:28Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-30T14:00:12Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-11T02:36:53Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-09T18:31:21Z",
          "name": "Hearings By (full committee)"
        }
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
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "DE"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1492is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1492\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Moreno (for himself, Ms. Blunt Rochester , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Secretary of Commerce support the leadership of the United States with respect to the deployment, use, application, and competitiveness of blockchain technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Deploying American Blockchains Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Advisory committee**\nThe term Advisory Committee means the National Blockchain Deployment Advisory Committee established pursuant to section 603(c).\n**(2) Blockchain technology or other distributed ledger technology**\nThe term blockchain technology or other distributed ledger technology means a distributed digital database where data is\u2014\n**(A)**\nshared across a network of computers to create a ledger of verified information among network participants;\n**(B)**\nlinked using cryptography to maintain the integrity of the ledger and to execute other functions; and\n**(C)**\ndistributed among network participants in an automated fashion to concurrently update network participants on the state of the ledger and other functions.\n**(3) Covered nongovernmental representative**\nThe term covered nongovernmental representative means a representative as specified in the second sentence of section 135(b)(1) of the Trade Act of 1974 ( 19 U.S.C. 2155(b)(1) ), except that such term does not include a representative of a non-Federal government.\n**(4) Secretary**\nThe term Secretary means the Secretary of Commerce.\n**(5) State**\nThe term State means each of the several States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe.\n**(6) Token**\nThe term token means a transferable, digital representation of information recorded on blockchain technology or other distributed ledger technology.\n**(7) Tokenization**\nThe term tokenization means the process of creating a token.\n#### 3. Department of commerce leadership on blockchain\n##### (a) Function of Secretary\nThe Secretary shall serve as a principal advisor to the President for policy pertaining to the deployment, use, application, and competitiveness of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization.\n##### (b) Activities\nThe Secretary shall support the leadership of the United States with respect to the deployment, use, application, and competitiveness of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization by organizing the Advisory Committee\u2014\n**(1)**\nto examine and to provide recommendations on issues and risks relating to the deployment, use, application, and competitiveness of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization, including the issues of decentralized identity, cybersecurity, key storage and security systems, artificial intelligence, fraud reduction, regulatory compliance, e-commerce, health care applications, and supply chain resiliency;\n**(2)**\nto support and to promote the improvement and security of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(3)**\nto help to promote the leadership of the United States with respect to the deployment, use, application, and competitiveness of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(4)**\nto promote the national security of the United States with respect to blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(5)**\nto support engagement with the public to develop a compendium of proposals for practices as part of the work described in subsection (d);\n**(6)**\nto consider policies to encourage coordination among Federal agencies with respect to the deployment of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(7)**\nto examine\u2014\n**(A)**\nhow Federal agencies can benefit from utilizing blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(B)**\nthe current use by Federal agencies of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(C)**\nthe current and future preparedness and ability of Federal agencies to adopt blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization; and\n**(D)**\nadditional security measures Federal agencies may need to take\u2014\n**(i)**\nto securely use blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization, including to support the security of critical infrastructure; and\n**(ii)**\nto enhance the resiliency of Federal systems against cyber threats to blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization; and\n**(8)**\nto support coordination of the activities of the Federal Government relating to the security of blockchain technology and other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization.\n##### (c) Establishment of national blockchain deployment advisory committee\n**(1) Establishment**\n**(A) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall, in consultation with the heads of relevant Federal agencies, establish an advisory committee to support the adoption of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization.\n**(B) Designation**\nThe advisory committee established pursuant to subparagraph (A) shall be known as the National Blockchain Deployment Advisory Committee .\n**(2) Membership composition**\nThe Advisory Committee shall consist of members appointed by the Secretary, which shall include\u2014\n**(A)**\nthe Secretary;\n**(B)**\nrepresentatives of Federal agencies (as determined necessary by the Secretary); and\n**(C)**\ncovered nongovernmental representatives with expertise related to blockchain technology or other distributed ledger technology (as determined necessary by the Secretary), which may include\u2014\n**(i)**\nblockchain technology or other distributed ledger technology infrastructure operators, suppliers, service providers, and vendors;\n**(ii)**\napplication developers building on blockchain technology or other distributed ledger technology;\n**(iii)**\ndevelopers and organizations supporting the advancement and deployment of public blockchain technology or other distributed ledger technology;\n**(iv)**\nsubject matter experts representing industrial sectors that can benefit from blockchain technology or other distributed ledger technology;\n**(v)**\nsmall, medium, and large businesses;\n**(vi)**\nthink tanks and academia;\n**(vii)**\nnonprofit organizations and consumer groups;\n**(viii)**\ncybersecurity experts;\n**(ix)**\nrural stakeholders;\n**(x)**\ncovered nongovernmental representatives; and\n**(xi)**\nartists and the content creator community.\n**(3) Termination of advisory committee**\nThe Advisory Committee shall terminate on the date that is 7 years after the date of the enactment of this Act.\n##### (d) Best practices\nThe Secretary shall, on an ongoing basis, facilitate and support the development of a compendium of identified or recommended guidelines or best practices for the deployment of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization that\u2014\n**(1)**\nsupport the deployment of technologies needed to advance the capabilities of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(2)**\nsupport the interoperability of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(3)**\nsupport operations, including hashing and key storage and security systems, that form the foundation of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(4)**\nreduce cybersecurity risks that may compromise blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization; and\n**(5)**\nquantify the value and potential cost savings associated with adoption of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization, including through comparative analyses of competing and existing technologies within specific industry applications.\n##### (e) Additional requirements\nIn carrying out this section, the Secretary shall\u2014\n**(1)**\nconsult closely and regularly with stakeholders, including private sector individuals and entities, and incorporate industry expertise;\n**(2)**\ncollaborate with private sector stakeholders to identify prioritized, flexible, repeatable, performance-based, and cost-effective approaches to the deployment of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(3)**\nmake public research and information pertaining to the use of, and marketplace for, blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(4)**\ndevelop standardized terminology for, and promote common understanding of, blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(5)**\nalign the recommendations of the compendium described in subsection (d) with the goal of facilitating the ease of use of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(6)**\nsupport open-source infrastructure, data management, and authentication activities with respect to blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization; and\n**(7)**\nconsider the needs and interests of both the private and public sector, including small businesses and Federal, State, and local governments.\n##### (f) Rules of construction\nNothing in this section may be construed\u2014\n**(1)**\nto require a private entity to share information with the Secretary;\n**(2)**\nto require a private entity to request assistance from the Secretary;\n**(3)**\nto require a private entity to implement any measure or recommendation suggested by the Secretary in response to a request by the private entity; or\n**(4)**\nto require the adoption of the best practices described in subsection (d).\n##### (g) Consultation\nIn implementing this section, the Secretary may, as appropriate, consult with the heads of relevant Federal agencies.\n#### 4. Reports to Congress\n##### (a) Interim reports\nNot later than 2 years after the date of the enactment of this Act, and annually thereafter, the Secretary shall make public on the website of the Department of Commerce and submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that includes\u2014\n**(1)**\na description of the activities of the Secretary under this title during the preceding year;\n**(2)**\nany recommendations by the Secretary for additional legislation to strengthen the competitiveness of the United States with respect to blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization; and\n**(3)**\na description of any emerging risks and long-term trends with respect to blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization.\n##### (b) Final report\nNot later than 18 months before the termination of the Advisory Committee pursuant to section 603(c)(3), the Secretary shall make available to the public on the website of the Department of Commerce and submit to the President, the Committee on Commerce, Science, and Transportation of the Senate, and the Committee on Energy and Commerce of the House of Representatives a final report containing the findings, conclusions, and recommendations of the Advisory Committee.",
      "versionDate": "2025-04-10",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1492rs.xml",
      "text": "II\nCalendar No. 195\n119th CONGRESS\n1st Session\nS. 1492\n[Report No. 119\u201384]\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Moreno (for himself, Ms. Blunt Rochester , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nOctober 21, 2025 Reported by Mr. Cruz , without amendment\nA BILL\nTo require the Secretary of Commerce support the leadership of the United States with respect to the deployment, use, application, and competitiveness of blockchain technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Deploying American Blockchains Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Advisory committee**\nThe term Advisory Committee means the National Blockchain Deployment Advisory Committee established pursuant to section 603(c).\n**(2) Blockchain technology or other distributed ledger technology**\nThe term blockchain technology or other distributed ledger technology means a distributed digital database where data is\u2014\n**(A)**\nshared across a network of computers to create a ledger of verified information among network participants;\n**(B)**\nlinked using cryptography to maintain the integrity of the ledger and to execute other functions; and\n**(C)**\ndistributed among network participants in an automated fashion to concurrently update network participants on the state of the ledger and other functions.\n**(3) Covered nongovernmental representative**\nThe term covered nongovernmental representative means a representative as specified in the second sentence of section 135(b)(1) of the Trade Act of 1974 ( 19 U.S.C. 2155(b)(1) ), except that such term does not include a representative of a non-Federal government.\n**(4) Secretary**\nThe term Secretary means the Secretary of Commerce.\n**(5) State**\nThe term State means each of the several States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe.\n**(6) Token**\nThe term token means a transferable, digital representation of information recorded on blockchain technology or other distributed ledger technology.\n**(7) Tokenization**\nThe term tokenization means the process of creating a token.\n#### 3. Department of commerce leadership on blockchain\n##### (a) Function of Secretary\nThe Secretary shall serve as a principal advisor to the President for policy pertaining to the deployment, use, application, and competitiveness of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization.\n##### (b) Activities\nThe Secretary shall support the leadership of the United States with respect to the deployment, use, application, and competitiveness of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization by organizing the Advisory Committee\u2014\n**(1)**\nto examine and to provide recommendations on issues and risks relating to the deployment, use, application, and competitiveness of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization, including the issues of decentralized identity, cybersecurity, key storage and security systems, artificial intelligence, fraud reduction, regulatory compliance, e-commerce, health care applications, and supply chain resiliency;\n**(2)**\nto support and to promote the improvement and security of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(3)**\nto help to promote the leadership of the United States with respect to the deployment, use, application, and competitiveness of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(4)**\nto promote the national security of the United States with respect to blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(5)**\nto support engagement with the public to develop a compendium of proposals for practices as part of the work described in subsection (d);\n**(6)**\nto consider policies to encourage coordination among Federal agencies with respect to the deployment of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(7)**\nto examine\u2014\n**(A)**\nhow Federal agencies can benefit from utilizing blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(B)**\nthe current use by Federal agencies of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(C)**\nthe current and future preparedness and ability of Federal agencies to adopt blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization; and\n**(D)**\nadditional security measures Federal agencies may need to take\u2014\n**(i)**\nto securely use blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization, including to support the security of critical infrastructure; and\n**(ii)**\nto enhance the resiliency of Federal systems against cyber threats to blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization; and\n**(8)**\nto support coordination of the activities of the Federal Government relating to the security of blockchain technology and other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization.\n##### (c) Establishment of national blockchain deployment advisory committee\n**(1) Establishment**\n**(A) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall, in consultation with the heads of relevant Federal agencies, establish an advisory committee to support the adoption of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization.\n**(B) Designation**\nThe advisory committee established pursuant to subparagraph (A) shall be known as the National Blockchain Deployment Advisory Committee .\n**(2) Membership composition**\nThe Advisory Committee shall consist of members appointed by the Secretary, which shall include\u2014\n**(A)**\nthe Secretary;\n**(B)**\nrepresentatives of Federal agencies (as determined necessary by the Secretary); and\n**(C)**\ncovered nongovernmental representatives with expertise related to blockchain technology or other distributed ledger technology (as determined necessary by the Secretary), which may include\u2014\n**(i)**\nblockchain technology or other distributed ledger technology infrastructure operators, suppliers, service providers, and vendors;\n**(ii)**\napplication developers building on blockchain technology or other distributed ledger technology;\n**(iii)**\ndevelopers and organizations supporting the advancement and deployment of public blockchain technology or other distributed ledger technology;\n**(iv)**\nsubject matter experts representing industrial sectors that can benefit from blockchain technology or other distributed ledger technology;\n**(v)**\nsmall, medium, and large businesses;\n**(vi)**\nthink tanks and academia;\n**(vii)**\nnonprofit organizations and consumer groups;\n**(viii)**\ncybersecurity experts;\n**(ix)**\nrural stakeholders;\n**(x)**\ncovered nongovernmental representatives; and\n**(xi)**\nartists and the content creator community.\n**(3) Termination of advisory committee**\nThe Advisory Committee shall terminate on the date that is 7 years after the date of the enactment of this Act.\n##### (d) Best practices\nThe Secretary shall, on an ongoing basis, facilitate and support the development of a compendium of identified or recommended guidelines or best practices for the deployment of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization that\u2014\n**(1)**\nsupport the deployment of technologies needed to advance the capabilities of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(2)**\nsupport the interoperability of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(3)**\nsupport operations, including hashing and key storage and security systems, that form the foundation of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(4)**\nreduce cybersecurity risks that may compromise blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization; and\n**(5)**\nquantify the value and potential cost savings associated with adoption of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization, including through comparative analyses of competing and existing technologies within specific industry applications.\n##### (e) Additional requirements\nIn carrying out this section, the Secretary shall\u2014\n**(1)**\nconsult closely and regularly with stakeholders, including private sector individuals and entities, and incorporate industry expertise;\n**(2)**\ncollaborate with private sector stakeholders to identify prioritized, flexible, repeatable, performance-based, and cost-effective approaches to the deployment of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(3)**\nmake public research and information pertaining to the use of, and marketplace for, blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(4)**\ndevelop standardized terminology for, and promote common understanding of, blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(5)**\nalign the recommendations of the compendium described in subsection (d) with the goal of facilitating the ease of use of blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization;\n**(6)**\nsupport open-source infrastructure, data management, and authentication activities with respect to blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization; and\n**(7)**\nconsider the needs and interests of both the private and public sector, including small businesses and Federal, State, and local governments.\n##### (f) Rules of construction\nNothing in this section may be construed\u2014\n**(1)**\nto require a private entity to share information with the Secretary;\n**(2)**\nto require a private entity to request assistance from the Secretary;\n**(3)**\nto require a private entity to implement any measure or recommendation suggested by the Secretary in response to a request by the private entity; or\n**(4)**\nto require the adoption of the best practices described in subsection (d).\n##### (g) Consultation\nIn implementing this section, the Secretary may, as appropriate, consult with the heads of relevant Federal agencies.\n#### 4. Reports to Congress\n##### (a) Interim reports\nNot later than 2 years after the date of the enactment of this Act, and annually thereafter, the Secretary shall make public on the website of the Department of Commerce and submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that includes\u2014\n**(1)**\na description of the activities of the Secretary under this title during the preceding year;\n**(2)**\nany recommendations by the Secretary for additional legislation to strengthen the competitiveness of the United States with respect to blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization; and\n**(3)**\na description of any emerging risks and long-term trends with respect to blockchain technology or other distributed ledger technology, applications built on blockchain technology or other distributed ledger technology, tokens, and tokenization.\n##### (b) Final report\nNot later than 18 months before the termination of the Advisory Committee pursuant to section 603(c)(3), the Secretary shall make available to the public on the website of the Department of Commerce and submit to the President, the Committee on Commerce, Science, and Transportation of the Senate, and the Committee on Energy and Commerce of the House of Representatives a final report containing the findings, conclusions, and recommendations of the Advisory Committee.",
      "versionDate": "2025-10-21",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-05-22T14:06:35Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2025-05-22T14:06:35Z"
          },
          {
            "name": "Broadcasting, cable, digital technologies",
            "updateDate": "2025-05-22T14:06:35Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2025-05-22T14:06:35Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-05-22T14:06:35Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-22T14:06:35Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2025-05-22T14:06:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-05-19T16:12:14Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1492is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1492rs.xml"
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
      "title": "Deploying American Blockchains Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T11:18:16Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Deploying American Blockchains Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-23T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Deploying American Blockchains Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-29T13:28:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Commerce support the leadership of the United States with respect to the deployment, use, application, and competitiveness of blockchain technology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-29T13:18:18Z"
    }
  ]
}
```
